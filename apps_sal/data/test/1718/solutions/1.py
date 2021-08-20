import collections
(n, k) = map(int, input().split())
a = list(map(int, input().split()))
c = collections.Counter(a)
length = n - c.most_common()[0][1] + 1
if length == 1:
    ans = 0
else:
    ans = (length + k - 3) // (k - 1)
print(ans)
