def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


n, k = [int(x) for x in input().split()]
a = [gcd(int(x), k) for x in input().split()]

if k == 1:
    print(((n + 1) * (n + 2)) // 2 - n - 1)
else:
    s = 0
    e = 0
    total = ((n + 1) * (n + 2)) // 2 - 1 - n
    # print(total)
    #extra = {}
    c = 1

    while e < n:
        flag = False
        while c % k != 0 and e < n:
            total -= e - s
            c *= a[e]
            e += 1
        while c % k == 0 and s < e:
            c //= a[s]
            s += 1
    total -= e - s
    print(total)
