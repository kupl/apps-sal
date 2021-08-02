n = int(input())
a = 0
b = 0
for i in range(n):
    x, y = list(map(int, input().split()))
    if (x >= y):
        a += 1
    if (x <= y):
        b += 1
if (a > b):
    print("Mishka")
if (a < b):
    print("Chris")
if (a == b):
    print("Friendship is magic!^^")
