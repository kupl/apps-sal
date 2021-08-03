n, x = map(int, input().split())
l = sorted([int(input()) for i in range(n)])
x -= sum(l)
ans = n
ans += x // l[0]
print(ans)
