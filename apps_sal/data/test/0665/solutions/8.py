for _ in range(int(input())):
    n, s = list(map(int, input().split()))
    a = tuple(map(int, input().split()))
    ans = 0
    ans1 = 0
    s1 = 0
    for i in range(n):
        if a[i] > a[ans]:
            ans = i
        s1 += a[i]
        if s1 > s:
            break
        ans1 += 1
    ans2 = 0
    s2 = 0
    for i in range(n):
        if i == ans:
            continue
        s2 += a[i]
        if s2 > s:
            break
        ans2 += 1
    if ans1 > ans2:
        print('0')
    else:
        print(ans + 1)
