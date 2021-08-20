t = int(input())
for _ in range(t):
    (a, b) = map(int, input().split())
    if a * 2 > b:
        print(-1, -1)
    else:
        print(a, 2 * a)
