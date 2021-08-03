n = int(input())
a = list(input())
xlist = [0]
x = 0
for i in range(n):
    if a[i] == "D":
        x -= 1
    elif a[i] == "I":
        x += 1
    xlist.append(x)
print(max(xlist))
