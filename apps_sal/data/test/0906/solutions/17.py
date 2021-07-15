a, b, c = [int(i) for i in input().split(' ')]

def exp_mod_prime(x, p):
    x = x % (p-1)
    a = 2
    bonus = 1
    while x > 1:
        if x % 2 == 1:
            bonus = (bonus * a) % p
        a = (a * a) % p
        x = x // 2
    return a * bonus % p

if c == 1:
    if a == 1:
        result = 1
    elif b == 1:
        result = 1
    else:
        result = exp_mod_prime((a-1) * (b-1), 1000000007)
else:
    if a == 1:
        if b % 2 == 0:
            result = 0
        else:
            result = 1
    elif b == 1:
        if a % 2 == 0:
            result = 0
        else:
            result = 1
    elif (a + b) % 2 == 1:
        result = 0
    else:
        result = exp_mod_prime((a-1) * (b-1), 1000000007)
    

print(result % 1000000007)

