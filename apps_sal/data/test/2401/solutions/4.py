t = int(input())
for _ in range(t):
    (n, r) = list(map(int, input().split()))
    s = sum(map(int, input().split()))
    x = 1
    while (s + x + r) % n != 0:
        x += 1
    print(x)
