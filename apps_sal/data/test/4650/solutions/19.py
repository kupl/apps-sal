q = int(input())
for i in range(q):
    n = int(input())
    l = list(map(int, input().split()))
    cnt1 = 0
    cnt0 = 0
    cnt2 = 0
    for j in range(n):
        if l[j] % 3 == 0:
            cnt0 += 1
        elif l[j] % 3 == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    cnt0 += min(cnt2, cnt1)
    tmp = cnt2
    cnt2 -= min(tmp, cnt1)
    cnt1 -= min(tmp, cnt1)
    print(cnt0 + cnt2 // 3 + cnt1 // 3)
