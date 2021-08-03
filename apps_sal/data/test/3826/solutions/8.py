'''n=int(input())
a=[int(i) for i in input().split()]
st = set()
pre=[]
for i in range(len(a)):
    st.add(a[i])
    pre.append(len(st))

stn=set()
suf=[]
for i in range(len(a)-1,-1,-1):
    stn.add(a[i])
    suf.append(len(stn))
suf = suf[::-1]
suf = suf + [0]
pre = [0]+pre
fuf = suf+[0]

ans=10**9
for i in range(len(a)):
    for j in range(i,len(a)):
        left=i
        right=j
        tot = (i) + (n-j-1)
        if(pre[i]+suf[j+1]==tot):
            print(i,j,left,right,tot,pre[i],suf[j])
            ans = min(ans,j-i+1)
if(ans==10**9):
    print(0)
else:
    print(ans)'''
from collections import defaultdict as dd


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    d = dd(int)

    for i in a:
        d[i] += 1

    cnt = 0
    ans = 10**9
    for i in d:
        if d[i] >= 2:
            cnt += 1

    if cnt == 0:
        print(0)
    else:
        for i in range(n):
            d2 = dd(int)
            ct = 0
            for j in range(i, n):
                d2[a[j]] += 1

                if d2[a[j]] == d[a[j]] - 1 and d[a[j]] >= 2:
                    ct += 1

                if ct == cnt:
                    ans = min(ans, abs(j - i + 1))

        print(ans)


main()
