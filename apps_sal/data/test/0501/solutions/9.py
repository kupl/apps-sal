from math import log

def howManyOdds(n):
    l = int(log(n+1, 2))
    if l%2 == 1:
        return (4**((l+1)//2) - 1) // 3
    else:
        return n - howManyEvens(n)

def howManyEvens(n):
    l = int(log(n+1, 2))
    if l%2 == 1:
        return n - howManyOdds(n)
    else:
        return (4**((l+1)//2) - 1) // 3 * 2

def firstEvens(n):
    return n * (n+1)

def firstOdds(n):
    return firstEvens(n) - n

def f(n):
    return firstEvens(howManyEvens(n)) + firstOdds(howManyOdds(n))

a, b = [int(i) for i in input().split()]
print((f(b) - f(a-1)) % (10**9 + 7))

