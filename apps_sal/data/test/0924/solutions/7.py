def gcd(x, y):
    if(y == 0):
        return x
    return gcd(y, x % y)


la, ra, ta = list(map(int, input().split()))

lb, rb, tb = list(map(int, input().split()))

gcd1 = gcd(ta, tb)
luca = ra - la + 1
lucb = rb - lb + 1
if((la - lb) % gcd1 == 0):
    print(min(luca, lucb))
else:

    # print(luca,lucb)
    op1 = lucb - (la - lb) % gcd1
    op2 = luca - (lb - la) % gcd1
    opf = max(op1, op2, 0)

    print(min(opf, luca, lucb))
