def gcd(a, b):
    if(b == 0):
        return a
    else:
        return(gcd(b, a % b))


def lcm(a, b):
    return a // gcd(a, b) * b


a, b = map(int, input().split())
b = 10**b
print(lcm(max(a, b), min(a, b)))
