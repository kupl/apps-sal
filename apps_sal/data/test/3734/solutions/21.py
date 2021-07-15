a = [28, 30, 31]
b = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
c = {}
for i in range(7):
    c[b[i]] = i
d1 = c[input()]
d2 = c[input()]
for i in a:
    if ((d1 + i) % 7) == d2:
        print("YES")
        return
print("NO")


