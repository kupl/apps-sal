from collections import Counter

N, K = map(int, input().split())
A = list(map(int, input().split()))

L = Counter(A)

ans = N
for a, cnt in L.most_common(K):
    ans -= cnt

print(ans)
