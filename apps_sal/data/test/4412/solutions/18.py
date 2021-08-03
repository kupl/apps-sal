def M(): return list(map(int, input().split()))


q = int(input())
for qer in range(q):
    n = int(input())
    a = M()

    D = {}

    for i in a:
        D[i] = 1

    a.sort(reverse=True)

    def get_max():
        for i in a:
            if D[i]:
                return i
        return 0

    def fix(x):
        for i in a:
            if x % i == 0:
                D[i] = 0

    L = [0] * 3
    for i in range(3):
        L[i] = get_max()
        if L[i] == 0:
            break
        fix(L[i])

    ans = sum(L)
    if a[0] % 2 == 0 and a[0] % 3 == 0 and a[0] % 5 == 0:
        if a[0] / 2 in D and a[0] / 3 in D and a[0] / 5 in D:
            ans = max(ans, a[0] // 2 + a[0] // 3 + a[0] // 5)

    print(ans)
