(A, B) = map(int, input().split())
w = '.'
b = '#'
ans = [[b] * 20 + [w] * 20 for _ in range(100)]
for i in range(A - 1):
    x = 2 * (i // 50)
    y = i % 50 * 2
    ans[y][x] = w
for i in range(B - 1):
    x = 2 * (i // 50) + 21
    y = i % 50 * 2
    ans[y][x] = b
print('100 40')
for i in range(100):
    print(''.join(ans[i]))
