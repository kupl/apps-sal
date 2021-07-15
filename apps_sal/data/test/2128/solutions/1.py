M = 998244353

def gcd(a, b):
    if (a == 0):
        return 0, 1

    x, y = gcd(b % a, a)

    return y - (b // a) * x, x



k = input()
probs = list(map(int, input().split(' ')))
num, denum = 0, 1
for p in probs:
    num = (num + denum) * 100 % M
    denum = denum * p % M

    #print(num, denum)

inv, _ = gcd(denum, M)
print(num * inv % M)


#d[i + 1] = (d[i] + 1) * 100 / p

