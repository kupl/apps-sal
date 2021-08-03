import collections
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
c = collections.Counter(a)
if len(c) < k:
    print(ans)
    return
l = c.most_common()
for i in range(1, -k + len(c) + 1):
    ans += l[-i][1]
print(ans)
