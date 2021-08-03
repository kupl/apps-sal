a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    u = x // y
    o = x % y
    print(u * y + min(o, y // 2))
