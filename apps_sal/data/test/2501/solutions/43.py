N = int(input())
A = list(map(int, input().split()))

p = [0] * N
m = [0] * N

for i in range(N):
    p[i] = A[i] + i + 1
    m[i] = i + 1 - A[i]

from collections import Counter

cp = Counter(p)
cm = Counter(m)

ans = 0

for x, y in cp.items():
    ans += cm[x] * y

print(ans)
