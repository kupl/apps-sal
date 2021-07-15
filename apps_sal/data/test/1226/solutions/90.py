def Li():
    return list(map(int, input().split()))


n, a, b = Li()
mod = pow(10, 9)+7
bunshi = 1
bunbo = 1
ans = pow(2, n, mod)-1
for i in range(a):
    bunshi = (bunshi*(n-i)) % mod
    bunbo = (bunbo*(i+1)) % mod
ans = (ans-bunshi*pow(bunbo, -1, mod)) % mod
for i in range(a, b):
    bunshi = (bunshi*(n-i)) % mod
    bunbo = (bunbo*(i+1)) % mod
ans = (ans-bunshi*pow(bunbo, -1, mod)) % mod
print(ans)

