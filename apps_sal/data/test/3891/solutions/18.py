(n, m) = map(int, input().split())
num = []
for i in range(n):
    num.append(input())
flag = False
for i in range(n):
    if flag:
        break
    for j in range(m):
        if flag:
            break
        fl = False
        if num[i][j] == 'B':
            u1 = j
            fl = True
            for x in range(j, m):
                if num[i][x] == 'B':
                    u2 = x
            if u1 == u2:
                ans1 = i
                ans2 = j
                flag = True
                break
            else:
                raw = (u2 + u1) // 2
                ans2 = raw
                ans1 = i + (u2 - u1) // 2
                flag = True
                break
print(ans1 + 1, ans2 + 1)
