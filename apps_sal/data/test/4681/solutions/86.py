n = int(input())
l = [2, 1]
for i in range(2, 90):
    x = l[i - 2] + l[i - 1]
    l.append(x)
print(l[n])
