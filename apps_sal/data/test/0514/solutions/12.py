q = int(input())
for ew in range(q):
    n, d = map(int, input().split())
    x = 0
    while (x + 10)**2 <= d:
        x += 1
    dup = 1
    for i in range(100):
        if (x + i) + (d + x + i) // (x + 1 + i) <= n:
            print("YES")
            dup = 0
            break
    if dup:
        print("NO")
