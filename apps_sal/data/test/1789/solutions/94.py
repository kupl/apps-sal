a,b,x,y=map(int,input().split())
cnt1=min(abs(a-b-1),abs(a-b))*y+x
cnt2=min(abs(a-b-1),abs(a-b))*2*x+x

print(min(cnt1, cnt2))
