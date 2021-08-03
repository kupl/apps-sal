a, b = map(int, input().split())
s = list(input())
dist = a * a + b * b
lis = [[0, 0]]
ver = hor = 0
for i in s:
    if i == 'U':
        ver += 1
    elif i == 'D':
        ver -= 1
    elif i == 'R':
        hor += 1
    else:
        hor -= 1
    lis.append([hor, ver])
flag = 1

if [a, b] in lis:
    print("Yes")
    return
for i in lis:
    if [a, b] == [i[0] + lis[-1][0], i[1] + lis[-1][0]]:
        print("Yes")
        return
for i in range(len(lis)):
    l = 0
    r = 100000000000
    c, d = lis[i]
    while l <= r:
        mid = l + (r - l) // 2
        e = mid * (lis[-1][0])
        f = mid * (lis[-1][1])
        if (e + c)**2 + (f + d)**2 < dist:
            l = mid + 1
        else:
            r = mid - 1
    if [l * (lis[-1][0]) + c, l * (lis[-1][1]) + d] == [a, b]:
        print("Yes")
        flag = 0
        break
    elif [r * (lis[-1][0]) + c, r * (lis[-1][1]) + d] == [a, b]:
        print("Yes")
        flag = 0
        break
if flag:
    print("No")
