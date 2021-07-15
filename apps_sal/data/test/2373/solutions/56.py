N=int(input())
p=list(map(int,input().split()))
cnt = 0
ans = 0
for i in range(1,len(p)+1):
    if i == p[i-1]:
        cnt += 1
    elif cnt == 1:
        ans += 1
        cnt = 0
    if cnt == 2:
        ans += 1
        cnt = 0
if cnt == 1:
    ans += 1
print(ans)
