s, x = map(int, input().split())
if s < x:
    print(0)
    return
f = x
if (s - x) % 2 == 1:
    print(0)
    return
x = bin(x)[2::]
y = (s - f) // 2
y = bin(y)
y = y[2:]
if len(x) > len(y):
    y = "0" * (len(x) - len(y)) + y
else:
    x = "0" * (len(y) - len(x)) + x
k = 0
for i in range(len(x)):
    if x[i] == "1":
        k += 1
    if int(x[i]) + int(y[i]) == 2:
        print(0)
        return
if s == f:
    print(2 ** k - 2)
    return
print(2 ** k)
