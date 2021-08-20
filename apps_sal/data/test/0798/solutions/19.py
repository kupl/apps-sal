v = list(map(int, input().split()))
found = False
for i in range(v[0] + 1):
    a = i
    b = v[0] - i
    if v[1] - a < 0 or v[2] - b < 0:
        continue
    if v[1] - a == v[2] - b:
        print(a, v[1] - a, b)
        found = True
        break
if not found:
    print('Impossible')
