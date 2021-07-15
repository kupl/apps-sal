for _ in range(int(input())):
    a, b, c, n = list(map(int, input().split()))
    a, b, c = sorted([a, b, c])
    delta = (c - a) + (c - b)
    if n >= delta and (n - delta) % 3 == 0:
        print("YES")
    else:
        print("NO")

