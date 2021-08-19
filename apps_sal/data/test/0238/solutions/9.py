n, m, k = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

bestbest = 0


def brute(n, m, k, A):
    ans = 0
    val = (0, 0)
    for i in range(n):
        for j in range(i, n):
            if ans < sum(A[i:j + 1]) - k * (ceil((j - i + 1) / m)):
                ans = sum(A[i:j + 1]) - k * (ceil((j - i + 1) / m))
                val = (i, j)
    return val, ans


for off in range(m):
    B = A[off:]
    C = []
    canstart = []
    for i in range(len(B)):
        if i % m == 0:
            C.append(-k)
            canstart.append(1)
        canstart.append(0)
        C.append(B[i])

    best = 0
    run = 0

    for i in range(len(C)):
        run += C[i]
        if run < -k:
            run = -k
        best = max(best, run)
    #print(best, C)
    bestbest = max(bestbest, best)

print(bestbest)
