n = int(input())
print((n * n + 1) // 2)
for i in range(n):
    s = ''
    for j in range(n):
        if (i + j) % 2 == 0:
            s += 'C'
        else:
            s += '.'
    print(s)
