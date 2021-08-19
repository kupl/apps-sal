for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    used = [False] * (n + 1)
    ans[0] = a[0]
    used[a[0]] = True
    lst = 1
    ok = True
    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans[i] = a[i]
            used[a[i]] = True
        elif a[i] < a[i - 1]:
            print(-1)
            ok = False
            break
        else:
            while used[lst]:
                lst += 1
            # print(lst)
            if a[i] < lst:
                print(-1)
                ok = False
                break
            else:
                ans[i] = lst
                lst += 1
                used[ans[i]] = True
    if ok:
        for i in range(n):
            print(ans[i], end=' ')
        print()
