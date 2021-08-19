import collections
(N, K) = map(int, input().split())
A = list(map(int, input().split()))
(values, counts) = zip(*collections.Counter(A).most_common())
ans = 0
B = counts[K:]
for i in B:
    ans += i
print(ans)
