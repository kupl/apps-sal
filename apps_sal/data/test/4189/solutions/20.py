n = int(input())
(a, b) = (0, 0)
for _ in range(n):
    (_, s) = input().split()
    if s == 'soft':
        a += 1
    else:
        b += 1
if a < b:
    (a, b) = (b, a)
x = 0
for i in range(1, 200):
    x += 1 + (i * 2 - 1) // 4 * 2
    if a <= x and b <= i ** 2 - x:
        print(i)
        break
