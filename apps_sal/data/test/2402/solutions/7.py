t = int(input())
for _ in range(t):
    (n, x, y) = map(int, input().split())
    if x + y - 1 <= n:
        maxi = x + y - 1
    else:
        maxi = n
    if max(x, y) < n:
        mini = 1 + max(0, x + y - n)
    elif x == y == n:
        mini = n
    else:
        mini = min(x, y) + 1
    print(mini, maxi)
