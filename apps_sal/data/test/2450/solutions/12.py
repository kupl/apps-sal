for _ in range(int(input())):
    n, m, x, y = tuple(map(int, input().split()))
    y = min(y, 2 * x)

    ans = 0
    for _ in range(n):
        line = [i for i in input()]

        i = 0
        while i < m:
            if line[i] == '.':
                if i != m - 1 and line[i + 1] == '.':
                    ans += y
                    i += 2
                else:
                    ans += x
                    i += 1
            else:
                i += 1

    print(ans)

