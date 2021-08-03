X, Y = list(map(int, input().split()))

for x in range(X + 1):
    if x * 2 + (X - x) * 4 == Y:
        print("Yes")
        break
else:
    print("No")
