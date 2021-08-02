t = int(input().strip())
for it in range(t):
    x, n, m = [int(i) for i in input().strip().split()]
    for i in range(n):
        if x <= 20:
            break
        x = x // 2 + 10
    x -= m * 10
    if x <= 0:
        print("YES")
    else:
        print("NO")
