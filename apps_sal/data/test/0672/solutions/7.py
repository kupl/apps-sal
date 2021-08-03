# -*- coding: utf-8 -*-
import random

a, b = list(map(int, input().split()))


def sums(s, l, b):
    if s > b:
        p = 1
        for x in l:
            p *= (x[1] + 1)
        #print("ok, s=",s,p)
        return p

    if not l:
        #print("malo: ", s)
        return 0
    #print(s, end=" ")

    p = 0
    for i in range(l[0][1] + 1):
        p += sums(s * (l[0][0]**i), l[1:], b)
    return p


def naive(a, b):
    if a == b:
        return "infinity"
    else:
        if a < b:
            return 0
        else:
            count = 0
            for x in range(1, a + 1):
                if a % x == b:
                    count += 1
            return count


def wise(a, b):
    if a == 1 and b == 0:
        return 1
    if a == b:
        return "infinity"
    else:
        d = a - b
        factors = {}
        i = 2
        while i * i <= d:
            if d % i == 0:
                factors.setdefault(i, 0)
                factors[i] += 1
                d //= i
            else:
                i += 1
        factors.setdefault(d, 0)
        factors[d] += 1

        return sums(1, list(factors.items()), b)

# for i in range(10000):
    # print(i)
    #a, b = map(int, input().split())
    ##a = random.randint(0,100000)
    ##b = random.randint(0,100000)
    # if wise(a, b) != naive(a, b):
        # print("!!!")
    #print(a, b, wise(a, b), naive(a, b))


print(wise(a, b))
