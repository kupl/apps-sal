t = int(input())
inputs = [input() for i in range(t)]


def solve(line):
    (n, x, y) = map(int, line.split())
    mx = max(min(n, x + y - 1), 1)
    mn = min(max(1, n - (n - x + (n - y) - 1)), n)
    print(str(mn) + ' ' + str(mx))


[solve(line) for line in inputs]
