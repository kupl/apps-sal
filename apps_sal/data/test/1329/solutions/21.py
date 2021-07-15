n = int(input())
if n==1:
    print(0)
    return
a = [0]*(n+1)
def pf(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
for i in range(2,n+1):
    x = pf(i)
    for j in x:
        a[j] += 1
b = [0]*5 #3,5,15,25,75
for i in a:
    if (i>=74):
        b[4]+=1
    elif (i>=24):
        b[3]+=1
    elif (i>=14):
        b[2]+=1
    elif (i>=4):
        b[1]+=1
    elif (i>=2):
        b[0]+=1
for i in range(4):
    b[3-i] += b[4-i]
ans = 0
ans += b[1]*(b[1]-1)//2*(b[0]-2)
ans += b[2]*(b[1]-1)
ans += b[3]*(b[0]-1)
ans += b[4]
print(ans)
