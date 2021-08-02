n = int(input())
a = list(map(int, input().split()))

x = [0] * len(a)
y = [0] * len(a)

c1 = 0
z1 = False
c2 = 0
z2 = False

for i in range(len(a)):
    if a[i] == 0:
        z1 = True
        c1 = 1
    elif z1:
        x[i] = c1
        c1 += 1
    else:
        x[i] = 0

    if a[n - i - 1] == 0:
        z2 = True
        c2 = 1
    elif z2:
        y[n - i - 1] = c2
        c2 += 1
    else:
        y[n - i - 1] = 0

ans = ""
for i in range(len(a)):
    if (x[i] == 0):
        if y[i] == 0:
            ans += "0 "
        else:
            ans += str(y[i]) + " "
    else:
        if y[i] == 0:
            ans += str(x[i]) + " "
        else:
            ans += str(min(x[i], y[i])) + " "
print(ans)
