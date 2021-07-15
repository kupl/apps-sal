n = int(input())
a = list(map(int,input().split()))

cnt_fu = 0
cnt_0 = 0
ans = 0
b = []
for i in range(n):
    ans += abs(a[i])
    b.append(abs(a[i]))
    if a[i]<0:
        cnt_fu += 1
    if a[i]==0:
        cnt_0 += 1
#print(cnt_fu,cnt_0,ans,b)
if cnt_fu%2==0:
    print(ans)
else:
    print((ans-min(b)*2))

