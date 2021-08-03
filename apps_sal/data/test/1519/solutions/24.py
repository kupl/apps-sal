n, l, a = map(int, input().split())
ans = 0
pr = 0
for i in range(n):
    d, c = map(int, input().split())
    ans += (d - pr) // a
    pr = d + c
ans += (l - pr) // a
print(ans)
