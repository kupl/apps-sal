n = int(input())
l = [int(x) for x in input().split()]
s = input() + '0'
i = minn = maxx = 0
flag = 0
while i < n:
    minn = maxx = l[i]
    start = i + 1
    while s[i] != '0':
        minn = min(minn, l[i])
        maxx = max(maxx, l[i])
        i += 1
    minn = min(minn, l[i])
    maxx = max(maxx, l[i])
    end = i + 1
    if minn >= start and maxx <= end:
        i += 1
    else:
        flag = 1
        break
if flag:
    print("NO")
else:
    print("YES")
