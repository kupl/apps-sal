(x, a), b = list(input().split()), 0

a = int(a)
x = list(map(int, list(str(x))))

for i in range(len(x) - 1):
    m = [-1, -1]

    if a > 0:
        if i + 1 + a > len(x):
            b = len(x)
        else:
            b = i + 1 + a
    else:
        break

    for j in range(i, b):
        if x[j] > m[0]:
            m[0] = x[j]
            m[1] = j

    del x[m[1]]
    x.insert(i, m[0])

    a = a - (m[1] - i)

x = list(map(str, x))

print( ''.join(x) )

