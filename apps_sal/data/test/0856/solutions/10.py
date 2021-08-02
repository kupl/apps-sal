def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    def do(u):
        j = max(u)
        return [j - i for i in u]
    b = []
    b.append(do(a))
    b.append(do(b[-1]))
    print(*b[(k - 1) % 2])


t = int(input())
for _ in range(t):
    solve()
