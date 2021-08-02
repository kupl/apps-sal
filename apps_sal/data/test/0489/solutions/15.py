from math import factorial
n = int(input())
a = [int(x) for x in input().split()]
web = 3
while web > 0:
    if a.count(min(a)) >= web:
        r = a.count(min(a))
        e = factorial(r)
        f = factorial(web) * factorial(r - web)
        e /= f
        print(int(e))
        return
    else:
        web -= a.count(min(a))
        e = min(a)
        while e in a:
            a.remove(e)
