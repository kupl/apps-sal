mod = 10**9+7
x, k = list(map(int, input().split(' ')))
if (x == 0):
    print(0)
else:
    val1 = pow(2,k+1,mod) * x
    val2 = pow(2, k, mod) - 1
    val1 -= val2
    val1 %= mod
    print(val1)

