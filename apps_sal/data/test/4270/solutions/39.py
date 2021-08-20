N = int(input())
v = list(map(int, input().split()))
v.sort()
while True:
    x = v[0]
    y = v[1]
    z = (x + y) / 2
    v.pop(0)
    v.pop(0)
    v.append(z)
    v.sort()
    if len(v) == 1:
        break
    else:
        pass
print(z)
