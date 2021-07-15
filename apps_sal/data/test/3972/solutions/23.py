import sys

n = int(input())
mod = 10 ** 9 + 7

if n == 1:
    print((1))
    return

lis = [0] * n
lis[0] = 1
bsum = 0
ans = min(n-1,2) + (n-1) ** 2



for i in range(n-1):

    i += 1

    lis[i] += lis[i-1]

    if i - 3 >= 0:
        bsum += lis[i-3]
        bsum %= mod

    lis[i] += bsum
    lis[i] %= mod

    if i != n-1:

        ans += lis[i] * ((n-1) ** 2)
        ans += lis[i] * min(n-1 , i+2)
        ans %= mod

    

ans += lis[-1] * n
ans %= mod

#print (lis)
print (ans)

