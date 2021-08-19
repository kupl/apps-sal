(n, k) = map(int, input().split())
l = sorted([int(x) for x in input().split()])
ans = 0
for i in range(len(l)):
    while 2 * k < l[i]:
        ans += 1
        k *= 2
    k = max(k, l[i])
print(ans)
