from collections import Counter
(N, M) = map(int, input().split())
A = list(map(int, input().split()))
A = Counter(A)
for _ in range(M):
    (b, c) = map(int, input().split())
    A[c] += b
A = sorted(A.items(), key=lambda x: x[0], reverse=True)
ans = 0
for (key, value) in A:
    if N - value >= 0:
        ans += key * value
        N -= value
    else:
        ans += N * key
        break
print(ans)
