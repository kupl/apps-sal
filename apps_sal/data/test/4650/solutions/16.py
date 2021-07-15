t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a = [i % 3 for i in a]
    c0 = a.count(0)
    c1 = a.count(1)
    c2 = a.count(2)
    x = min(c1, c2)
    c1 -= x
    c2 -= x
    s = c0 + x + c1 // 3 + c2 // 3
    print(s)

