def solve(L):
    if not L:
        return 0
    if 0 not in L:
        return min(L) + solve([l - min(L) for l in L])
    tmp = 0
    (l, p) = (0, False)
    for i in range(len(L)):
        if L[i] == 0:
            if p:
                p = False
                tmp += solve(L[l:i])
                l = i + 1
            else:
                l = i + 1
        elif not p:
            p = True
    return tmp + solve(L[l:])


N = int(input())
H = list(map(int, input().split()))
print(solve(H))
