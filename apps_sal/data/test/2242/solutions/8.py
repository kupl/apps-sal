
def solve():
    s=input().split()[0]
    cnt=[0]*2020
    cnt[0]=1
    m=0
    t=1
    for d in map(int,s[-1::-1]) :
        m=(m+d*t)%2019
        t=(t*10)%2019
        cnt[m]+=1
    return sum([ k*(k-1)//2 for k in cnt])

print((solve()))

