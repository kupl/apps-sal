from sys import stdin, stdout
import sys
input = sys.stdin.readline


def solve(n, t, tasks):
    lo = 0
    hi = n

    res = []
    curr_res = 0

    tasks.sort(key=lambda x: x[1])

    while lo <= hi:
        mid = lo + (hi - lo) // 2

        valid_tasks = []
        for i in tasks:
            if i[0] >= mid:
                valid_tasks.append(i)

        can_do = False

        curr_sum = 0
        total_used = 0
        r = []
        for i in valid_tasks:
            curr_sum += i[1]
            total_used += 1
            r.append(i[2])
            if curr_sum > t:
                break
            elif total_used >= mid:
                can_do = True
                curr_res = mid
                res = r
                break
        if can_do:
            lo = mid + 1
        else:
            hi = mid - 1
    return curr_res, res


def main():
    n, t = (int(x) for x in input().split(" "))
    tasks = []
    nums = n
    idx = 1
    while n:
        a_i, t_i = (int(x) for x in input().split(" "))
        tasks.append((a_i, t_i, idx))
        idx += 1
        n -= 1
    res, res_arry = solve(nums, t, tasks)
    print(res)
    print(res)
    stdout.write(" ".join(map(str, res_arry)))
    stdout.write("\n")


def __starting_point():
    main()


__starting_point()
