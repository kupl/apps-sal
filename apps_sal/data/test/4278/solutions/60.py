import math


def comb(n, r):
    if n - r >= 0:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
    else:
        return 0


n = int(input())
l = []
for i in range(n):
    s = sorted(input())
    l.append(s)
l.sort()
cnt = 1
ans = 0

for i in range(n - 1):
    if l[i] == l[i + 1]:
        cnt += 1
    else:
        ans += comb(cnt, 2)
        cnt = 1

ans += comb(cnt, 2)

print(ans)
