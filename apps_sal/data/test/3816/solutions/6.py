#in the name of god
#Mr_Rubick
a,b,c,l=list(map(int, input().split()))
cnt=(l+3)*(l+2)*(l+1)//3
for i in (a,b,c):
    s=2*i-a-b-c
    for x in range(max(0,-s),l+1):
        m = min(s+x,l-x)
        cnt-=(m+1)*(m+2)
print(cnt//2)

