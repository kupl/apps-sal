(n, m) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ac = bc = 0
for item in a:
    if item % 2 == 0:
        bc += 1
for item in b:
    if item % 2 == 0:
        ac += 1
print(min(ac, n - bc) + min(bc, m - ac))
