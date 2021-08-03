N = int(input())
vlist = list(map(int, input().split()))
vlist.sort()
ans = 0
for i in range(N):
    if i == 0:
        ans += vlist[i]
    else:
        ans = (ans + vlist[i]) / 2
print(ans)
