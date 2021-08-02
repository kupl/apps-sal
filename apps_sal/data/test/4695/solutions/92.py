x, y = map(int, input().split())
if x in {1, 3, 5, 7, 8, 10, 12}:
    x = 1
elif x in {4, 6, 9, 11}:
    x = 2
else:
    x = 3
if y in {1, 3, 5, 7, 8, 10, 12}:
    y = 1
elif y in {4, 6, 9, 11}:
    y = 2
else:
    y = 3
print("Yes" if x == y else "No")
