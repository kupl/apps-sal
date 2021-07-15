n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    ss = min(c // 2, b)
    b -= ss
    tt = min(b // 2, a)
    print((ss + tt) * 3)
