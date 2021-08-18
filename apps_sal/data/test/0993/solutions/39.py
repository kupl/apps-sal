from collections import Counter

n, m = map(int, input().split())
A = list(map(int, input().split()))

B = [0] * (n + 1)

for i in range(n):
    B[i + 1] = B[i] + A[i]

li = [i % m for i in B]

C = Counter(li)

ans = 0
for v in C.values():
    if v > 1:
        ans += v * (v - 1) // 2

print(ans)
