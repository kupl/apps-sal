
lpn = int(input())

for loop in range(lpn):

    n = int(input())
    p = list(map(int, input().split()))

    for i in range(n):

        if p[i] == 1:
            oneind = i
            break

    l = oneind
    r = oneind
    nmax = 1
    ans = [0] * n
    ans[0] = 1

    for i in range(n - 1):

        if l == 0 or (r != n - 1 and p[l - 1] > p[r + 1]):
            r += 1
            nmax = max(nmax, p[r])
            if i + 2 == nmax:
                ans[i + 1] = 1
        else:
            l -= 1
            nmax = max(nmax, p[l])

            if i + 2 == nmax:
                ans[i + 1] = 1

    print("".join(map(str, ans)))
