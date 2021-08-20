t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    d = (a + b) // 3
    while (d + 1) * 3 <= a + b:
        d += 1
    print(min(min(d, a), b))
