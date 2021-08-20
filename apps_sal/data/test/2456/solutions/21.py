t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    if a > b:
        print(b * (b + 1) // 2)
    else:
        print(a * (a - 1) // 2 + 1)
