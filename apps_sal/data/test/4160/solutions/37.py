x=int(input())
ans=0
cnt=0
t=100
while(True):
    cnt += 1
    t*=101
    t//=100
    # print(t)
    if x<=t:
        print(cnt)
        return

