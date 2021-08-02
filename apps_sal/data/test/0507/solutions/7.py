n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
bad = []


def isok(tmp):
    s = set()
    for i in range(len(tmp)):
        s.add(tmp[i])
    return len(s) == n


for i in range(len(a)):
    if a[i] != b[i]:
        bad.append(i)
if len(bad) == 1:
    k = [0] * (n + 1)
    for i in range(len(a)):
        if i != bad[0]:
            k[a[i]] = 1
    rs = 0
    for i in range(1, n + 1):
        if not k[i]:
            rs = i
            break
    tmp = []
    for i in range(len(a)):
        if i != bad[0]:
            tmp.append(a[i])
        else:
            tmp.append(rs)
    print(*tmp)

else:
    tmp = []
    tmp1 = []
    for i in range(len(a)):
        if i == bad[0]:
            tmp.append(b[i])
            tmp1.append(a[i])
        else:
            tmp.append(a[i])
            tmp1.append(b[i])
    if isok(tmp):
        print(*tmp)
    else:
        print(*tmp1)
