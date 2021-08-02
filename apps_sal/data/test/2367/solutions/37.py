
# Function to find modulo inverse of b. It returns
# -1 when inverse doesn't
# modInverse works for prime m
def gcd(b, m):
    if b == 0:
        return m
    return gcd(m % b, b)


def modInverse(b, m):
    g = gcd(b, m)
    if (g != 1):
        # print("Inverse doesn't exist")
        return -1
    else:
        # If b and m are relatively prime,
        # then modulo inverse is b^(m-2) mode m
        return pow(b, m - 2, m)


# Function to compute a/b under modulo m
def modDivide(a, b, m):
    a = a % m
    inv = modInverse(b, m)
    if(inv == -1):
        print("Division not defined")
    else:
        return (inv * a) % m


MOD = (10 ** 9) + 7
H, W, A, B = list(map(int, input().split(' ')))

DP = []
j = 1
for i in range(1, 200002):
    j *= i
    j %= MOD
    DP.append(j)

# print(DP)


def factorial(i):
    if (i == 0):
        return 1
    nonlocal DP
    # print(i)
    # print(i, DP[i-1])
    # print(DP[i-1])
    return DP[i - 1]


def move2(H, W, A, B):
    numPaths = 0
    h = H - A
    w = W - (W - B) + 1
    a = A + 1
    pttp = 0
    for b in range(w, W + 1):
        # print(h, b, a, W-b+1)
        ttp = (factorial(h + b - 2) * modInverse((factorial(h - 1) * factorial(b - 1)) % MOD, MOD)) % MOD
        tpttp = ttp
        ttp -= pttp
        pttp = tpttp
        btp = (factorial(a + (W - b + 1) - 2) * modInverse((factorial(a - 1) * factorial(W - b)) % MOD, MOD)) % MOD
        # btp = factorial(a+(W-b+1)-2)//(factorial(a-1)*factorial(W-b))
        numPaths += ttp * btp
    return numPaths


ways = move2(H, W, A, B)
print(ways % (10**9 + 7))
