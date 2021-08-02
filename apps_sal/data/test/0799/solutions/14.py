n = int(input())
l = [int(x) for x in input().split()]
mx = max(l)
ans = 0
for e in l:
    ans += mx - e
print(ans)
