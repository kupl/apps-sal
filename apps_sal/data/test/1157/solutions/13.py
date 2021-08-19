def solve(a, n):
    neg = [0 for i in range(n)]
    pos = [0 for i in range(n)]
    if a[0] < 0:
        neg[0] = 1
    else:
        pos[0] = 1
    for i in range(1, n):
        if a[i] < 0:
            neg[i] += 1 + pos[i - 1]
            pos[i] += neg[i - 1]
        else:
            pos[i] += 1 + pos[i - 1]
            neg[i] += neg[i - 1]
    totalNeg = 0
    totalPos = 0
    for i in range(n):
        totalNeg += neg[i]
        totalPos += pos[i]
    return (totalNeg, totalPos)


n = int(input())
a = list(map(int, input().split()))
(l, r) = solve(a, n)
print(str(l) + ' ' + str(r))
