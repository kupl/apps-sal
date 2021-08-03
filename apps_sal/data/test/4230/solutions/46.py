x, n = list(map(int, input().split()))
p = list(map(int, input().split()))
y = x
z = x
if x not in p:
    print(x)
    return
for i in range(2 * len(p)):
    y -= 1
    z += 1
    if y not in p:
        print(y)
        return
    if z not in p:
        print(z)
        return
