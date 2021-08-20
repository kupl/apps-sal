n = int(input())
L = []
for _ in range(n):
    (x, y) = [int(x) - 1 for x in input().split()]
    L.append((x, y))
if n == 3:
    print('1 2 3')
else:
    order = ['1']
    count = 1
    current = 0
    while count < n:
        (a, b) = L[current]
        if b in L[a]:
            order.append(str(a + 1))
            count += 1
            current = a
        else:
            order.append(str(b + 1))
            count += 1
            current = b
    print(' '.join(order))
