n, a, b = map(int, input().split())
mod = 10**9+7

x = 1
d = [2]
m = n
for i in range(30):
    if m&1:
        x *= d[-1]
        x %= mod
    m >>= 1
    d.append(d[-1]**2%mod)

l = n
inverse = [0, 1]
g = [1, 1]
for i in range(2, 4**9):
    if i == a+1:
        x -= l*g[-1]%mod
    if i == b+1:
        x -= l*g[-1]%mod
        break
    l *= n-i+1
    l %= mod
    inverse.append((-inverse[mod%i]*(mod//i))%mod)
    g.append(g[-1]*inverse[-1]%mod)

print((x-1)%mod)
