n = int(input())
a = int(input())
b = int(input())
c = int(input())

l = 0
while n >= a or n >= b:
    if n >= b and b - c < a:
        nl1 = (n - b) // (b - c)
        nl2 = n // b
        nl = max(nl1, nl2)
        l += nl
        n -= (b - c) * nl
    else:
        nl = n // a
        l += nl
        n -= a * nl

print(l)

