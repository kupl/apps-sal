def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return a * b // gcd(a, b)

def lcml(a):
    if len(a) == 1:
        return a[0]
    else:
        return lcm(a[0], lcml(a[1:]))

n = int(input())
print((lcml(list(range(2, n+1)))+1))

