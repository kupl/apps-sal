n, m = map(int, input().split(" "))
a = [list(map(int, input().split(" "))) for i in range(n)]
b = [list(map(int, input().split(" "))) for i in range(m)]

for ax, ay in a:
    c = []
    for bx, by in b:
        c.append(abs(bx - ax) + abs(by - ay))
    print(c.index(min(c)) + 1)
