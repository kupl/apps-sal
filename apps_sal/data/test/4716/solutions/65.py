N, K = map(int, input().split())
l = [int(x) for x in input().split()]
l.sort()
l.reverse()
ans = 0
for i in range(K):
    ans += l[i]
print(ans)
