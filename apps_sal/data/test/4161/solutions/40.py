from math import gcd

K = int(input())


ans = 0
for i in range(1, K+1):
    for j in range(1, K+1):
        tmp = gcd(i, j)
        if tmp == 1:
            ans += tmp*K
        else:
            for k in range(1, K+1):
                ans += gcd(tmp, k)
            

print(ans)
