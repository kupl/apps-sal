(a, b, c) = list(map(int, input().split()))
x = a
y = 0
done = False
while x >= 0:
    if b - y == c - x and c - x >= 0:
        print(y, b - y, x)
        done = True
        break
    x -= 1
    y += 1
if not done:
    print('Impossible')
