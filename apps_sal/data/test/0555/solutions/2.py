new = ''
a = int(input())
a = str(a)
t = len(a)
for i in range(t):
    if i == 0:
        if int(a[i]) <= 4 or int(a[i]) == 9:
            new += str(a[i])
        else:
            new += str(9-int(a[i]))
    else:
        if int(a[i]) <= 4:
            new += str(a[i])
        else:
            new += str(9-int(a[i]))
print(new)

