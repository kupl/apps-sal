h, w, d = map(int, input().split())
pos = [-1 for _ in range(h * w)]

for i in range(h):
    alst = list(map(int, input().split()))
    for j, a in enumerate(alst):
        pos[a - 1] = [i, j]
dif = [0 for _ in range(h * w)]
check = [False for _ in range(h * w)]

for num in range(h * w):
    if check[num]:
        continue
    check[num] = True
    total = 0
    dif[num] = total
    for j in range(num + d, h * w, d):
        dx = pos[j][0] - pos[j - d][0]
        dy = pos[j][1] - pos[j - d][1]
        dd = abs(dx) + abs(dy)
        total += dd
        dif[j] = total
        check[j] = True
        
for _ in range(int(input())):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(abs(dif[l] - dif[r]))
