(N,) = list(map(int, input().split()))
for _ in range(N):
    s = input().strip()
    x = [0] * (len(s) + 1)
    y = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        if s[i - 1] == '1':
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
    r1 = r2 = len(s)
    for i in range(1, len(s) + 1):
        r1 = min(r1, x[i - 1] + (y[-1] - y[i]))
        r2 = min(r2, y[i - 1] + (x[-1] - x[i]))
    print(min(r1, r2))
