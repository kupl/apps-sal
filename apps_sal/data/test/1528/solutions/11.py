import sys
sys.setrecursionlimit(100000000)

N, K = map(int, input().split())

store = [pow(2, i + 1) - 1 for i in range(51)]


def maisu(n):
    return pow(2, n + 2) - 3


def burger(n, k):  # n層でk枚
    if k == maisu(n):
        return store[n]
    elif k <= 1:
        return 0
    elif (maisu(n) - 3) // 2 + 1 >= k:
        return burger(n - 1, k - 1)
    else:
        # print(k-(2+maisu(n-1)),maisu(n-1))
        return burger(n - 1, k - (2 + maisu(n - 1))) + burger(n - 1, maisu(n - 1)) + 1


ans = burger(N, K)
print(ans)
