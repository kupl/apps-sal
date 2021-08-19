import sys
input = sys.stdin.readline
for _ in range(int(input())):
    (a, b, c) = list(map(int, input().split()))
    ans = 10 ** 18
    index = [0, 0, 0]
    for x in range(1, c + 1):
        for y in range(x, c + 100, x):
            cost = abs(a - x) + abs(b - y)
            if c % y < y - c % y:
                z = c - c % y
                cost += c % y
            else:
                z = c + (y - c % y)
                cost += y - c % y
            if ans > cost:
                ans = cost
                index = [x, y, z]
    print(ans)
    print(*index)
