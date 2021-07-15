n = int(input())
a = list(map(int,input().split()))

ans = 0

chk = {4:0,8:1,15:2,16:3,23:4,42:5}

ct = [0]*6
for i in a:
    if i not in [4,8,15,16,23,42]:
       ans+=1
for i in a:
    if i in [4,8,15,16,23,42]:
       if i==4:
          ct[0]+=1
       else:
           if ct[chk[i]-1]>ct[chk[i]]:
              ct[chk[i]]+=1
           else:
              ans+=1
ans1 = ct[5]
for i in ct:
    ans += (i-ans1)
print(ans)
