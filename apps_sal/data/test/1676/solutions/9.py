3


n, b = map(int, input().split())

ends = []

for i in range(n):
    t, d = map(int, input().split())

    while len(ends) > 0 and ends[0] <= t:
        ends.pop(0)

    q = len(ends) - 1

    if q == b:
        print(-1, end=' ')
        continue

    if not ends:
        ends.append(t + d)
    else:
        ends.append(ends[-1] + d)

    print(ends[-1], end=' ')
