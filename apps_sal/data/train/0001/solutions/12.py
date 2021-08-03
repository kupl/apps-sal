q = int(input())

Q = [list(map(int, input().split())) for i in range(q)]

for n, m, k in Q:
    if n > k or m > k:
        print(-1)
        continue

    x = max(n, m) - min(n, m)
    y = k - max(n, m)

    if x % 2 == 0 and y % 2 == 0:
        print(k)
    elif x % 2 == 0 and y % 2 == 1:
        print(k - 2)
    elif x % 2 == 1 and y % 2 == 0:
        print(k - 1)
    elif x % 2 == 1 and y % 2 == 1:
        print(k - 1)
