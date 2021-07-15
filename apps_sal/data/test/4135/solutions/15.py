def d(n):
    z = [1]
    for i in range(2,n//2+1):
        if n%i==0:
            z.append(i)
    z.append(n)
    return z
n = int(input())
t = list(input())
z = d(n)
#z.reverse()
for i in z:
    k = t[:i]
    k.reverse()
    t = k + t[i:]
for i in range(n):
    print(t[i],end='')
