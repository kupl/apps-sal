n = int(input())
x = int(round(n ** 0.5 - 0.499999))
y = x - 9999
while x >= y and x > 0:
    list_1 = list(map(int, str(x)))
    s = 0
    for i in list_1:
        s = s + i
    if x * x + s * x - n == 0:
        print(x)
        break
    else:
        x = x - 1
if not x * x + s * x - n == 0:
    print('-1')
