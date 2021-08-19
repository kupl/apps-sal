(a, b) = map(int, input().split())
print(100, 100)
for i in range(50):
    s = []
    for j in range(100):
        if (i + j) % 3 == 0 and (b - 1) * i > 0:
            s.append('#')
            b -= 1
        else:
            s.append('.')
    print(*s, sep='')
for i in range(50):
    s = []
    for j in range(100):
        if (i + j) % 3 == 0 and (a - 1) * i > 0:
            s.append('.')
            a -= 1
        else:
            s.append('#')
    print(*s, sep='')
