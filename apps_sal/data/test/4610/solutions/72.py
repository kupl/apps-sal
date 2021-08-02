import collections
N, K = map(int, input().split())
A = list(map(int, input().split()))
a = collections.Counter(A)
b = a.most_common()
ans = 0
if len(b) > K:
    for i in range(K, len(b)):
        ans += b[i][1]
print(ans)
