n = int(input())
a = []
b = []
asum = 0
bsum = 0
temp = 0
for i in range(n):
    temp = int(input())
    if temp > 0:
        asum += temp
        a.append(temp)
    else:
        bsum += -temp
        b.append(-temp)
if asum != bsum:
    print("first") if asum > bsum else print("second")
else:
    if a == b:
        print("first") if temp > 0 else print("second")
    else:
        print("first") if a > b else print("second")
