n, r = list(map(int, (input().split())))

plus = []
minn = []

for i in range(0, n):

    temp = list(map(int, input().split()))

    if temp[1] <= 0:
        temp.append(temp[0] + temp[1])
        minn.append(temp)
    else:
        plus.append(temp)

plus.sort()
minn.sort(reverse=True, key=lambda x: x[2])
flag = True
for i in plus:

    if i[0] <= r:
        r += i[1]
    else:
        flag = False
        break
if flag:
    for i in minn:
        if i[0] <= r:
            r += i[1]
        else:
            flag = False
            break


if flag and r >= 0:
    print("YES")
else:
    print("NO")
