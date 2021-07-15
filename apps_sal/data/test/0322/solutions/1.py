n = int(input())
l = 0
r = 0
for i in range(n):
    x, y = [int(i) for i in input().split()]
    if x > 0:
        l += 1
    else:
        r += 1
if l <= 1 or r <= 1:
    print("Yes")
else:
    print("No")

