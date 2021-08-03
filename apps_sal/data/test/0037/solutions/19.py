a, b, c = list(map(int, input().split()))
x1 = c // a + 1
f = False
for i in range(x1):
    j = (c - a * i) // b
    #print(i, i*a, j, b * j, c - a*i)
    if a * i + b * j == c:
        f = True
if f:
    print("Yes")
else:
    print("No")
