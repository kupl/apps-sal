n = int(input())
if n % 2 == 0:
    print(n * n // 2)
else:
    print(((n + 1) // 2)**2 + (n // 2)**2)
for i in range(n):
    c = []
    for j in range(n):
        if i % 2 == 0:
            if j % 2 == 0:
                c.append('C')
            else:
                c.append('.')
        else:
            if j % 2 == 0:
                c.append('.')
            else:
                c.append('C')
    print(''.join(c))
