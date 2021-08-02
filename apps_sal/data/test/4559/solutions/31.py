n = int(input())
a = sorted([int(x) for x in input().split()])

if a[0] == 0: print(0); return
ans = 1
for ai in a:
    ans *= ai
    if ans > 10**18: print(-1); break
else:
    print(ans)
