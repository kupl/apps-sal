n = int(input())
print((n * n + 1) // 2)
for i in range(n):
    print(''.join(('C' if (i + j) % 2 == 0 else '.' for j in range(n))))
