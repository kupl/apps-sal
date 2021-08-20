from collections import Counter
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
A = Counter(A).most_common()
s = 0
for i in range(min(K, len(A))):
    s += A[i][1]
print(N - s)
