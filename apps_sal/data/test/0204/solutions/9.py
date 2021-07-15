def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

a,b,x,y = list(map(int,input().split()))


val  = gcd(x, y)
x //= val
y //= val

a_min = a // x
b_min = b // y

print(min(a_min, b_min))

