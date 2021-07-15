def mi():
    return list(map(int, input().split()))
'''
7
aacdeee
'''
n = int(input())
s = list(input())

i,c1 = 0,1
while i+1<n and s[i+1]==s[i]:
    c1+=1
    i+=1

i = n-1
c2 = 1
while i-1>=0 and s[i-1]==s[i]:
    c2+=1
    i-=1

if s[0]!=s[-1]:
    print(c1+c2+1)
else:
    if c1==n:
        print((n*(n+1)//2)%998244353)
    else:
        print(((c1+1)*(c2+1))%998244353)

