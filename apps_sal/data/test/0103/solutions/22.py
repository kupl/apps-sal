def user99():
    n = int(input())
    a = list(map(int, input().split()))
    b = [[] for i in range(n)]

    ptr = 0
    for i in range(n):
        if i >= 1 and a[i - 1] + 1 != a[i]:
            ptr += 1
        b[ptr].append(a[i])

    ans = 0
    for i in b:
        if len(i) == 0:
            continue;
        x = len(i) - 2
        if i[0] == 1: x += 1
        if i[-1] == 10**3: x += 1
        ans = max(ans, x)

    print(ans)

user99()
