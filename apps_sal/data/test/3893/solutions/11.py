x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))

ans = 0
for i in range(int(input())):
    a, b, c = list(map(int, input().split()))
    if (a * x1 + b * y1 + c) * (a * x2 + b * y2 + c) < 0:
        ans += 1

print(ans)

