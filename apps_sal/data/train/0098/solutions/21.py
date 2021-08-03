q = int(input())
for i in range(q):
    c, m, x = map(int, input().split())
    print(min(min(c, m), (c + m + x) // 3))
