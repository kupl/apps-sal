from collections import Counter
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
B = [0]
for i in range(N):
    B.append((B[-1] + A[i]) % M)
C = Counter(B)
ans = 0
for (mod, c) in C.most_common():
    ans += c * (c - 1) // 2
print(ans)
