from sys import stdin

def inverse(a,mod):
    return pow(a,mod-2,mod)

n = int(stdin.readline())
c = list(map(int,stdin.readline().split()))

mod = 998244353
c.sort()
d = [0]
for i in range(n):
    d.append(d[-1] + c[i])

inv = inverse( n , mod )
ans = []

for k in range(1,n+1):

    now = 0

    ni = n-k
    cnt = 1
    while ni > k:
        now += cnt * (d[ni]-d[ni-k])
        cnt += 1
        ni -= k
    now += cnt * d[ni]
    ans.append(now * inv % mod)

print (*ans)
