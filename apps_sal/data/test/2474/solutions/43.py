import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


n = int(input())
a = list(map(int, input().split()))
a.sort()
a = a[::-1]
M = 10**9 + 7
ans = 0
ans += a[0] * (pow(2, 0, M)) * pow(2, n - 1, M)
for i in range(1, n):
    num = a[i]
    ans += num * (pow(2, i, M) + i * pow(2, i - 1, M)) * pow(2, n - i - 1, M)
    ans %= M
ans *= pow(2, n, M)
ans %= M
print(ans)
