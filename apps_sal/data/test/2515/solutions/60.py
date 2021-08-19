from math import sqrt
import bisect


def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    sqrtNum = sqrt(num)
    for i in range(3, int(sqrtNum) + 1, 2):
        if num % i == 0:
            return False
    return True


def solve(query):
    ans = []
    al = []
    for i in range(3, 10 ** 5 + 1, 2):
        if is_prime(i) and is_prime((i + 1) // 2):
            al.append(i)
    for q in query:
        if is_prime(q[0]) and is_prime((q[0] + 1) // 2):
            l_ind = bisect.bisect_right(al, q[0]) - 1
        else:
            l_ind = bisect.bisect_right(al, q[0])
        if is_prime(q[1]) and is_prime((q[1] + 1) // 2):
            r_ind = bisect.bisect_left(al, q[1])
        else:
            r_ind = bisect.bisect_left(al, q[1]) - 1
        ans.append(r_ind - l_ind + 1)
    return ans


def __starting_point():
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]
    ans = solve(query)
    for a in ans:
        print(a)


__starting_point()
