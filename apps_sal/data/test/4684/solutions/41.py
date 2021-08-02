r, g, b = list(map(int, input().split()))
a = 100 * r + 10 * g + b
if a % 4 == 0:
    print("YES")
else:
    print("NO")
