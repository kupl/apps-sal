K = int(input())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


result = 0

for a in range(1, K + 1):
    result += a
    #print('{} add'.format(a))
    b = a + 1
    while b <= K:
        result += 6 * gcd(a, b)
        #print('{} and {} add'.format(a, b))
        l = gcd(a, b)
        c = b + 1
        while c <= K:
            result += 6 * gcd(l, c)
            #print('{} and {} and {} add'.format(a, b, c))
            c += 1
        b += 1
print(result)
