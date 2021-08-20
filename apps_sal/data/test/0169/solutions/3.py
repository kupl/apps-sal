n = int(input())
a = int(input())
b = int(input())
c = int(input())
cost1 = a
cost2 = b - c
if cost1 <= cost2:
    print(n // cost1)
else:
    r = 0
    if n >= b:
        t = (n - b + 1) // cost2
        r += t
        n -= t * cost2
        if n >= b:
            n -= cost2
            r += 1
    r += n // cost1
    print(r)
