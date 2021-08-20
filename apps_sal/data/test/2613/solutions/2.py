for i in ' ' * int(input()):
    (n, k, z) = map(int, input().split())
    L = list(map(int, input().split()))
    mx = sum(L[:k + 1])
    sumL = []
    for j in range(n - 1):
        sumL.append(L[j] + L[j + 1])
    for j in range(z):
        if k <= 2 * j + 1:
            break
        count = max(sumL[:k - 2 * j - 1]) * (j + 1) + sum(L[:k + 1 - 2 * (j + 1)])
        if count > mx:
            mx = count
    print(mx)
