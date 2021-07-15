n = int(input())
a = [0] * 1001
a[0] = 0
a[1] = 1
d = set()
d.add(0)
d.add(1)
for i in range(2, 1001):
    a[i] = a[i - 1] + a[i - 2]
    d.add(a[i])
s = ""
for i in range(1, n + 1):
    if i in d:
        s += "O"
    else:
        s += "o"
print(s)
