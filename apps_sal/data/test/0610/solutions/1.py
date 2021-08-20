3
(n, m) = tuple(map(int, input().split()))


def solve(start, r, b):
    i = 0
    while r and b:
        i += 1
        if i % 2 == 0:
            if start[-1] == 'r':
                start.append('r')
                r -= 1
            else:
                start.append('b')
                b -= 1
        elif start[-1] == 'r':
            start.append('b')
            b -= 1
        else:
            start.append('r')
            r -= 1
    if r:
        start.extend(['r'] * r)
    if b:
        start.extend(['b'] * b)
    return (len([1 for (f, s) in zip(start[:-1], start[1:]) if f == s]), len([1 for (f, s) in zip(start[:-1], start[1:]) if f != s]))


print(*max(solve(['r'], n - 1, m), solve(['b'], n, m - 1)))
