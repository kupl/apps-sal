tsh = list(map(int, input().split()))
need = [[0, 0] for i in range(6)]
n = int(input())
ans = [[0, False] for i in range(n)]
for i in range(n):
    req = input().split(",")
    ans[i][1] = len(req) > 1
    if len(req) == 1:
        if req[0] == 'S':
            need[0][0] += 1
            ans[i][0] = 0
        elif req[0] == 'M':
            need[1][0] += 1
            ans[i][0] = 1
        elif req[0] == 'L':
            need[2][0] += 1
            ans[i][0] = 2
        elif req[0] == 'XL':
            need[3][0] += 1
            ans[i][0] = 3
        elif req[0] == 'XXL':
            need[4][0] += 1
            ans[i][0] = 4
        elif req[0] == 'XXXL':
            need[5][0] += 1
            ans[i][0] = 5
    else:
        if req[0] == 'S':
            need[0][1] += 1
            ans[i][0] = 0
        elif req[0] == 'M':
            need[1][1] += 1
            ans[i][0] = 1
        elif req[0] == 'L':
            need[2][1] += 1
            ans[i][0] = 2
        elif req[0] == 'XL':
            need[3][1] += 1
            ans[i][0] = 3
        elif req[0] == 'XXL':
            need[4][1] += 1
            ans[i][0] = 4
        elif req[0] == 'XXXL':
            need[5][1] += 1
            ans[i][0] = 5
next = 0
new = [[0, 0] for i in range(6)]
for i in range(6):
    tsh[i] -= need[i][0]
    tsh[i] -= next
    new[i][0] = next + need[i][0]
    if tsh[i] < 0:
        print("NO"); quit()
    can = min(tsh[i], need[i][1])
    next = need[i][1] - can
    new[i][1] = next
print("YES")
for x in ans:
    if x[1] and new[x[0]][1] > 0:
        new[x[0]][1] -= 1
        x[0] += 1
    t = x[0]
    if t == 0:
        print("S")
    elif t == 1:
        print("M")
    elif t == 2:
        print("L")
    elif t == 3:
        print("XL")
    elif t == 4:
        print("XXL")
    elif t == 5:
        print("XXXL")
