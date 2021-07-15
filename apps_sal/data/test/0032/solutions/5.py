import sys

n = int(input())

cur = 0

for _ in range(n):
    a, b = input().split()
    a = int(a)
    if b == "North":
        cur -= a
    elif b == "South":
        cur += a
    elif cur == 0 and b != "South":
        print("NO")
        return
    elif cur == 20000 and b != "North":
        print("NO")
        return
    if not 0 <= cur <= 20000:
        print("NO")
        return

if cur != 0:
    print("NO")
else:
    print("YES")

