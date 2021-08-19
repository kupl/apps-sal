t = int(input())
for _ in range(t):
    (a, b, c, d) = map(int, input().split())
    nokori = a - b
    if a - b <= 0:
        print(b)
    else:
        diff = c - d
        if diff <= 0:
            print(-1)
        else:
            cnt = -(-nokori // diff)
            print(b + cnt * c)
