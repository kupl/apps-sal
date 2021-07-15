"""
NTC here
"""
from sys import stdin

def iin(): return int(stdin.readline())
 
 
def lin(): return list(map(int, stdin.readline().split()))


# range = xrange
# input = raw_input


def main():
    t=iin()
    while t:
        t-=1
        n=iin()
        a=lin()
        m=iin()
        h=[lin()[::-1] for i in range(m)]
        h.sort(reverse=True)
        a1=[[j,i] for i,j in enumerate(a)]
        a2=[-1]*n
        a1.sort()
        i=0
        j=0
        while j<n and i<m:
            if h[i][1]>=a1[j][0]:
                a2[a1[j][1]]=i
                j+=1
            else:
                i+=1
        if -1 in a2:
            print(-1)
        else:
            dp=[1]*n
            for i in range(1,n):
                ad=[0]
                ch=0
                if h[a2[i]][0]>dp[i-1]:
                    if h[a2[i]][1]>=h[a2[i-1]][1]:
                        ad.append(dp[i-1])
                        ch+=1
                if h[a2[i-1]][0]>dp[i-1]:
                    if h[a2[i-1]][1]>=h[a2[i]][1]:
                        ad.append(dp[i-1])
                        if ch==0:
                            a2[i]=a2[i-1]
                dp[i]+=max(ad)
            print(dp.count(1))
            # print(dp,a2,h)













main()
# try:
#     main()
# except Exception as e: print(e)

