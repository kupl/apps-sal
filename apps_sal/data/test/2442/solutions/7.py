def solve():
    n = int(input())
    a = list(map(int, input().split()))
    u = 0
    for i in range(n + 1):
        if a.count(i) < 2:
            u = i
            break
    v = 0
    for i in range(n + 1):
        if a.count(i) < 1:
            v = i
            break
    print(u + v)


t = int(input())
for _ in range(t):
    solve()
