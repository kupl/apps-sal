(a, b, c) = [int(x) for x in input().split()]
f = True
for i in range(c // a + 1):
    for j in range((c - i) // b + 1):
        if i * a + j * b == c:
            f = False
            break
    if not f:
        break
if not f:
    print('Yes')
else:
    print('No')
