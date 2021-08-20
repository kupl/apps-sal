n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split(' '))))
c = 0
left = 0
for i in range(n):
    if i == 0:
        c += 1
        left = l[0][0]
        continue
    elif l[i][0] - l[i][1] > left:
        c += 1
        left = l[i][0]
        continue
    elif not i == n - 1:
        if l[i][0] + l[i][1] < l[i + 1][0]:
            c += 1
            left = l[i][0] + l[i][1]
            continue
        else:
            left = l[i][0]
    elif i == n - 1:
        c += 1
        break
    else:
        left = l[i][0]
        continue
print(c)
