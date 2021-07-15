n = int(input())
y = 0
for i in range(n):
    t, d = input().split()
    t = int(t)
    if d == "South":
        if y + t > 20000 or y == 20000:
            print("NO")
            raise SystemExit
        y += t
    if d == "North":
        if y - t < 0 or y == 0:
            print("NO")
            raise SystemExit
        y -= t
    if d == "West" or d == "East":
        if y == 0 or y == 20000:
            print("NO")
            raise SystemExit
if y != 0:
    print("NO")
    raise SystemExit
print("YES")

