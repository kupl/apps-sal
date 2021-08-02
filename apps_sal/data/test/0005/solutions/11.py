n, pos, l, r = map(int, input().split())


def solve(n, pos, l, r):
    if l == 1 and r == n:
        return 0
    elif l == 1:
        return abs(pos - r) + 1
    elif r == n:
        return abs(pos - l) + 1
    else:
        if l <= pos and pos <= r:
            return abs(r - l) + min(abs(pos - l), abs(pos - r)) + 2
        elif pos < l:
            return abs(pos - l) + abs(r - l) + 2
        else:
            return abs(pos - r) + abs(r - l) + 2


print(solve(n, pos, l, r))
