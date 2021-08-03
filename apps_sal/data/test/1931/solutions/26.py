def check(x, n):
    used = 2 * x
    used += (3 * x * (x - 1) // 2)

    if used <= n:
        return True

    return False


def find(n):
    low = 0
    high = n
    h = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid, n):
            h = mid
            low = mid + 1
        else:
            high = mid - 1

    used = 2 * h
    used += 3 * h * (h - 1) // 2
    return used


def solve(n, ans):
    total = 0
    while n > 0:
        used = find(n)
        # print(used)
        if used > 0:
            total += 1
            n -= used
        else:
            break

    ans.append(total)


def main():
    t = int(input())
    ans = []
    for i in range(t):
        n = int(input())
        solve(n, ans)

    for i in ans:
        print(i)


main()
