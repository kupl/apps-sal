q = int(input())
cnt1 = 0
cnt2 = 0
flag = 0
a = list(map(int, input().split()))
l = a[0]
for i in range(q):
    if a[i] == 0:
        if l != a[i] and cnt1 != 0 and (cnt2 != 0):
            if cnt1 != cnt2:
                flag = 1
            cnt1 = 0
        cnt1 += 1
    else:
        if l != a[i] and cnt2 != 0 and (cnt1 != 0):
            if cnt1 != cnt2:
                flag = 1
            cnt2 = 0
        cnt2 += 1
    l = a[i]
if cnt1 != cnt2 and cnt1 != 0 and (cnt2 != 0):
    flag = 1
if flag == 1:
    print('NO')
else:
    print('YES')
