import math
def derange(n): return int(math.factorial(n) * sum([((-1)**i) / math.factorial(i) for i in range(n + 1)]))


def choose(n, k):
    ans = 1
    if n - k < k:
        k = n - k
    for i in range(k):
        ans *= (n - i)
    ans /= math.factorial(k)
    return int(ans)


def almostIdent(n, k):
    ans = 0
    for i in range(k + 1):
        ans += choose(n, n - i) * derange(i)
    return ans


s = input().split(" ")
n = int(s[0])
k = int(s[1])
print(almostIdent(n, k))
