N = int(input())
n = list(map(int, input().split()))
m = int(sum(n) / N)


def fun(x):
    ans = 0
    for i in n:
        ans += (i - x) ** 2
    return ans


s = min(fun(m), fun(m + 1))
print(s)
