n = int(input())
a = [int(_) for _ in input().split()]
ans1 = 0
ans2 = 0
tmp1 = 0
tmp2 = 0

flag = False
for i in a:
    tmp1 += i
    if flag and tmp1 <= 0:
        ans1 += 1 - tmp1
        tmp1 = 1
    elif not flag and tmp1 >= 0:
        ans1 += tmp1 + 1
        tmp1 = -1

    if flag:
        flag = False
    else:
        flag = True

flag = True
for i in a:
    tmp2 += i
    if flag and tmp2 <= 0:
        ans2 += 1 - tmp2
        tmp2 = 1
    elif not flag and tmp2 >= 0:
        ans2 += tmp2 + 1
        tmp2 = -1

    if flag:
        flag = False
    else:
        flag = True

print(min(ans1, ans2))
