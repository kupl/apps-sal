from sys import stdin

tt = int(stdin.readline())
pls = []

for loop in range(tt):

    n, q = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    a = [0] + a + [0]

    lis = [0] * len(a)

    ans = 0
    for i in range(1, len(a) - 1):
        if a[i - 1] < a[i] and a[i] > a[i + 1]:
            lis[i] = 1
            ans += a[i]
        elif a[i - 1] > a[i] and a[i] < a[i + 1]:
            lis[i] = -1
            ans -= a[i]

    pls.append(ans)

    for loop in range(q):

        l, r = list(map(int, stdin.readline().split()))
        if l == r:
            pls.append(ans)
            continue
        ch = {}
        ch[l - 1] = 0
        ch[l] = 0
        ch[l + 1] = 0
        ch[r - 1] = 0
        ch[r] = 0
        ch[r + 1] = 0

        for i in ch:
            ans -= a[i] * lis[i]

        a[l], a[r] = a[r], a[l]

        for i in ch:
            if i == 0 or i == len(a) - 1:
                pass
            elif a[i - 1] < a[i] and a[i] > a[i + 1]:
                lis[i] = 1
                ans += a[i]
            elif a[i - 1] > a[i] and a[i] < a[i + 1]:
                lis[i] = -1
                ans -= a[i]
            else:
                lis[i] = 0
        pls.append(ans)

print("\n".join(map(str, pls)))
