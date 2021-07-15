ra, rb, rc = map(int, input().split())
a = min(ra, rb, rc)
c = max(ra, rb, rc)
b = ra + rb + rc - a - c

if (a + b) > c:
    print(0)
else:
    print(c + 1 - a - b)
