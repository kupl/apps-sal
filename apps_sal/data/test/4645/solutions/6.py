def solve(l, r):
    n = r - l + 1
    if n == 0:
        return []
    elif n % 4 == 0:
        return [l + 1, l + 3, l, l + 2] + solve(l + 4, r)
    elif n % 4 == 1:
        return [l] + solve(l + 1, r)
    elif n % 4 == 2:
        return [l] + solve(l + 1, r - 1) + [r]
    return [5, 1, 3, 6, 2, 4, 7] + solve(l + 7, r)


t = int(input())
for i in range(t):
    n = int(input())
    if n <= 3:
        print(-1)
    else:
        print(*solve(1, n))
