from collections import Counter
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
total = 0
for v in C.values():
    total += v * (v - 1) // 2

for a in A:
    x = C[a] * (C[a] - 1) // 2
    ans = total - x
    ans += (C[a] - 1) * (C[a] - 2) // 2
    print(ans)
