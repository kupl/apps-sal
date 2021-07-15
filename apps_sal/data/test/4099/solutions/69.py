n,k,m = map(int,input().split())
li = list(map(int,input().split()))
su = sum(li)
x = m*n -su
if x > k:
    print('-1')
elif x < 0:
    print(0)
else:
    print(x)
