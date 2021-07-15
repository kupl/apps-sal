n = int(input())
i = 1
while n:
    if i > 1:
        print(' ', end='')
    if n == 3:
        print(*[i, i, i * 3], end='')
        break
    print(' '.join([str(i)] * ((n + 1) // 2)), end='')
    i <<= 1
    n >>= 1

print()

