def mainA():
    T = int(input())
    for i in range(T):
        L, v, l, r = map(int, input().split())
        ans = L // v
        dow = l // v * v
        up = r // v * v
        if dow < l:
            dow += v
        ans -= max((up - dow) // v + 1, 0)
        print(ans)


def mainB():
    n, r = map(int, input().split())
    a = [int(e) for e in input().split()]
    r -= 1
    fr = 0
    ans = 0
    while fr < n:
        i = min(fr + r, n - 1)
        flag = False
        while i >= max(fr - r, 0) and not flag:
            if a[i] == 1:
                ans += 1
                fr = i + r + 1
                flag = True
                break
            i -= 1
        if not flag:
            print(-1)
            return
    print(ans)


mainB()
