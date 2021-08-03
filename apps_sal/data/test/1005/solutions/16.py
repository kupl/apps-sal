t = int(input())
for i in range(t):
    n, k, d = list(map(int, input().split()))
    mass = [int(i) - 1 for i in input().split()]
    arr = [0 for z in range(k)]
    kol = 0
    for j in range(d):
        if arr[mass[j]] == 0:
            kol += 1
        arr[mass[j]] += 1
    minn = kol
    for j in range(d, n):
        if arr[mass[j - d]] == 1:
            kol -= 1
        arr[mass[j - d]] -= 1
        if arr[mass[j]] == 0:
            kol += 1
        arr[mass[j]] += 1
        minn = min(minn, kol)
    print(minn)
