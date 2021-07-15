import sys
input=sys.stdin.readline
def count(a, b):
    m = len(a)
    n = len(b)
    lookup = [[0] * (n + 1) for i in range(m + 1)]
    for i in range(n+1):
        lookup[0][i] = 0
    for i in range(m + 1):
        lookup[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
            else:
                lookup[i][j] = lookup[i - 1][j]

    return lookup[m][n]
n=int(input())
s=input()
ans=0
z=0
for i in s:
    if(i=='?'):
        z+=1
n1=count(s,"abc")
ans=ans+(pow(3,z,1000000007)*n1)

n1=count(s,"?bc")
if(z>=1):
    ans=ans+(pow(3,z-1,1000000007)*n1)
n1=count(s,"a?c")
if(z>=1):
    ans=ans+(pow(3,z-1,1000000007)*n1)
n1=count(s,"ab?")
if(z>=1):
    ans=ans+(pow(3,z-1,1000000007)*n1)
n1=count(s,"??c")
if(z>=2):
    ans=ans+(pow(3,z-2,1000000007)*n1)
n1=count(s,"a??")
if(z>=2):
    ans=ans+(pow(3,z-2,1000000007)*n1)
n1=count(s,"?b?")
if(z>=2):
    ans=ans+(pow(3,z-2,1000000007)*n1)
n1=count(s,"???")
if(z>=3):
    ans=ans+(pow(3,z-3,1000000007)*n1)
print(ans%1000000007)
