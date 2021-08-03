n = int(input(""))
a = []
b = []
for i in range(n):
    x, y = input("").split()
    a.append(int(x))
    b.append(int(y))
max = 0
for i in range(n):
    for j in range(i + 1, n):
        if (a[i] - a[j])**2 > max:
            max = (a[i] - a[j])**2
            d = {"a": max}
        if (b[i] - b[j])**2 > max:
            max = (b[i] - b[j])**2
            d = {"a": max}


print(d["a"])
