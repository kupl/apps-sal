n = int(input())
a, b = 0, 0
for i in map(int, input().split()):
    if i % 4 == 0:
        a += 1
    elif i % 2 == 0:
        b += 1
c = n - a - b
if b == 0:
    if a + 1 < c:
        print("No")
    else:
        print("Yes")
else:
    if a < c:
        print("No")
    else:
        print("Yes")
