t = int(input())

for i in range(t):
    n, x, y, d = list(map(int, input().split()))
    w = []
    if x % d == y % d:
        w.append(abs(y - x) // d)
    if y % d == 1 % d:
        w.append(((x + d - 1) // d + y // d))
    if y % d == n % d:
        w.append((n - x + d - 1) // d + (n - y) // d)
    if w:
        print(min(w))
    else:
        print(-1)
