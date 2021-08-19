for _ in range(int(input())):
    (n, s, k) = map(int, input().split())
    l = [*map(int, input().split())]
    dic = set(l)
    cnt = 0
    flag1 = False
    for i in range(s, n + 1):
        if i not in dic:
            flag1 = True
            break
        else:
            cnt += 1
    cnt1 = 0
    flag = False
    for i in range(s, 0, -1):
        if i not in dic:
            flag = True
            break
        else:
            cnt1 += 1
    if flag and flag1:
        print(min(cnt, cnt1))
    elif flag1:
        print(cnt)
    else:
        print(cnt1)
