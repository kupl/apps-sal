n = int(input())
a = list(map(int, input().split()))
cnt = 0
cnt1 = 0
cnt2 = 0
p = -1
flag = True
for i in range(n):
    if a[i] == 1:
        if p != 1:
            if cnt != cnt1 and cnt != 0:
                flag = False
            cnt = cnt1
            p = 1
            cnt1 = 0
        cnt1 += 1
    if a[i] == 0:
        if p != 0:
            if cnt != cnt1 and cnt != 0:
                flag = False
            cnt = cnt1
            cnt1 = 0
            p = 0
        cnt1 += 1
if cnt != cnt1 and cnt != 0:
    flag = False
if flag:
    print('YES')
else:
    print('NO')
