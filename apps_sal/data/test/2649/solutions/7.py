def solve(n, x, y):
    z = [u + v for u, v in zip(x, y)]
    w = [u - v for u, v in zip(x, y)]
    return max([max(z) - min(z), max(w) - min(w)])


n = int(input())
x, y = zip(*[map(int, input().split()) for i in range(n)])
print(solve(n, x, y))
