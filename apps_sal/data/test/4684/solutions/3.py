r, g, b = input().split()
n = r + g + b
if int(n) % 4 == 0:
    print("YES")
else:
    print("NO")
