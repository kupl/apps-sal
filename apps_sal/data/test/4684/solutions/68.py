r, g, b = list(map(int, input().split()))
num = r * 100 + g * 10 + b * 1
if num % 4 == 0:
    print("YES")
else:
    print("NO")
