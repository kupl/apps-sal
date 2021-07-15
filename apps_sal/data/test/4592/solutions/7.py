import collections

n = int(input())
mod = 10**9+7

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

d = collections.defaultdict(int)
for i in range(2,n+1):
    for j in factorization(i):
        d[j[0]] += j[1]

ans = 1
for v in d.values():
    ans *= (v+1)
print(ans%mod)
