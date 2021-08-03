a, b, c = list(map(int, input().split()))
f = False
for na in range(1 + c // a):
    if f:
        break
    for nb in range(1 + c // b):
        if a * na + b * nb == c:
            f = True
            break
if f:
    print("Yes")
else:
    print("No")
