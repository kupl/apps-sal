n, l, r = list(map(int, input().split()))
c0 = (r//3*3-l//3*3)//3+1
c1 = (r//3*3-l//3*3)//3
c2 = (r//3*3-l//3*3)//3
if(l%3==1):
    c0-=1
elif(l%3==2):
    c0-=1
    c1-=1
if(r%3==1):
    c1+=1
elif(r%3==2):
    c2+=1
    c1+=1
cnt0 = [c0]
cnt1 = [c1]
cnt2 = [c2]
for i in range(n):
    cnt0.append((cnt0[i]*c0+cnt1[i]*c2+cnt2[i]*c1)%1000000007)
    cnt1.append((cnt0[i]*c1+cnt1[i]*c0+cnt2[i]*c2)%1000000007)
    cnt2.append((cnt0[i]*c2+cnt1[i]*c1+cnt2[i]*c0)%1000000007)
print(cnt0[-2]%1000000007)

