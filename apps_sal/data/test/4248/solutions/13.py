a = int(input())
s = 0
for i in range(a):
    s += float(input().split()[1])
d = round(s / a, 3) + 5
l = len(str(d).split(".")[1])
if l < 3:
    print(str(d) + "0" * (3 - l))
else:
    print(d)
