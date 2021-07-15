mod = 10**9+7
n=int(input())
a=input()
b=input()
c=input()
d=input()
x = a+b+c+d
if x=='BABB' or x=='BBAA' or x=='BABA' or x=='ABAA':
    c = max(n-3,0)
    ans = pow(2,c,mod)
    print(ans)
elif x=='BBBA' or x=='ABBA' or x=='BAAB' or x=='BAAA':
    f = [1,1]
    for j in range(n-3):
        x = (f[-1]+f[-2])%mod
        f.append(x)
    print((f[n-2]))

else:
    print((1))

