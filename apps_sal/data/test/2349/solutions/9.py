def solve():
    n = int(input())
    s = set()
    s.add(0)
    for i in range(1, int(n ** 0.5) + 1):
        k = n // i
        s.add(k)
        s.add(i)
    ans = sorted(s)
    print(len(ans))
    print(*ans)


t = int(input())
for i in range(t):
    solve()
