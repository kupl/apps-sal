(r1, c1, r2, c2) = list(map(int, input().split()))
if r1 == r2 or c1 == c2:
    n1 = 1
else:
    n1 = 2
if (r1 + c1) % 2 != (r2 + c2) % 2:
    n2 = 0
elif r1 + c1 == r2 + c2 or r1 - c1 == r2 - c2:
    n2 = 1
else:
    n2 = 2
print(n1, n2, max(abs(r1 - r2), abs(c1 - c2)))
