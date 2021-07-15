MOD = 10**9 + 7

def solve(s, p=13):
    a = [0] * p
    a[0] = 1
    for c in s:
        b = [0] * p
        for i in range(p):
            b[(i*10)%p] = a[i] % MOD
        b += b
        if c == "?":
            for i in range(p):
                a[i] = sum(b[i+4:i+p+1])
        else:
            for i in range(p):
                a[i] = b[i+p-int(c)]
    return a[5] % MOD

s = input()
print(solve(s))
