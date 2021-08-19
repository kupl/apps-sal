t = int(input())
for _ in range(t):
    s = input()
    n = len(s)
    ans = 0
    grid = [0] * (n + 1)
    score = 0
    maxmin = 0
    for i in range(n):
        if s[i] == '-':
            score -= 1
        else:
            score += 1
        maxmin = min(maxmin, score)
    score = 0
    for i in range(n):
        if s[i] == '-':
            score -= 1
        else:
            score += 1
        if -1 * score - 1 >= 0:
            if grid[-1 * score - 1] == 0:
                grid[-1 * score - 1] = i + 1
    for i in range(-1 * maxmin, n):
        grid[i] = 0
    grid[n] = n
    print(sum(grid))
