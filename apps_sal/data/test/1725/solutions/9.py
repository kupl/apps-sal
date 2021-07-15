def solve(d, l):
    l.sort()
    m = l[0] % d
    median = len(l) // 2
    res = 0
    for num in l:
        if num % d != m:
            return -1
        res += abs(num - l[median]) // d
    return res

def __starting_point():
    f = lambda: list(map(int, input().split()))
    n, m, d = f()
    l = []
    for i in range(n):
        l += f()
    print(solve(d, l))

__starting_point()
