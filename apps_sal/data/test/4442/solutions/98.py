a, b = map(int, input().split())

(x, y) = (a, b) if a<=b else (b, a)

for _ in range(y):
    print(x, end='')
