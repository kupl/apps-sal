def solve():
    (x, y) = map(int, input().split())
    (a, b) = map(int, input().split())
    d = abs(x - y)
    a1 = a * (x + y)
    a2 = b * min(x, y) + a * d
    print(min(a1, a2))


for i in range(int(input())):
    solve()
