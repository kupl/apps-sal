x, y = map(int, input().split())
for i in range(0, x + 1):
    if 2 * i + 4 * (x - i) == y:
        print("Yes")
        break
else:
    print("No")
