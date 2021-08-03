x, k = list(map(int, input().split()))
mod = 1000000007
if (k == 0):
    print((2 * x) % mod)
elif (x == 0):
    print(0)
else:
    ans = ((2 * x - 1) * pow(2, k, mod) + 1) % mod
    print(ans)
