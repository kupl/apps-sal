(n, k) = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
l.reverse()
assert l.__len__() == n
ans = 0
for i in range(k):
    ans += l[i]
print(ans)
