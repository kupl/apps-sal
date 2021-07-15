n , k = list(map(int, input().split()))
a = list(map(int,input().split()))
a.sort()

MOD = 1000000007

factorial = [1]
inverse = [1]
for i in range(1, n+2):
    factorial.append(factorial[-1] * i % MOD)
    inverse.append(pow(factorial[-1], MOD - 2, MOD))

def combi(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD

max_sum=0
min_sum=0

for i in range(k-1,n):
    t = combi(i,k-1)
    max_sum+=a[i]*t
    max_sum%=MOD
    min_sum+=a[n-i-1]*t
    min_sum%=MOD
if max_sum-min_sum<0:
    max_sum+=MOD
print((max_sum-min_sum))

