import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
res = [0] * n
a = sorted(a, reverse=True)
ai = 0
for i in range(0, n, 2):
    res[i] = a[ai]
    ai += 1
if n % 2 == 0:
    res[-1] = a[ai]
    ai += 1
for i in range(1, n - 1, 2):
    res[i] = a[ai]
    ai += 1
ans = 0
for i in range(n):
    if not (i - 1 >= 0 and i + 1 < n):
        continue
    if res[i] < res[i - 1] and res[i] < res[i + 1]:
        ans += 1
print(ans)
print(*res)
