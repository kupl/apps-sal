n = int(input())
x = {}
for i in range(n):
    l = input()
    try:
        x[l[0]].append(l)
    except:
        x[l[0]] = [l]
p = 0
for (k, v) in x.items():
    a = len(v) // 2
    b = len(v) - a
    p += (a - 1) * a / 2
    p += (b - 1) * b / 2
print(int(p))
