(n, x, y) = list(map(int, input().split()))
arr = list(map(int, input().split()))
for nowi in range(n):
    now = arr[nowi]
    check = True
    for i in range(x):
        if nowi - 1 - i < 0:
            break
        if arr[nowi - 1 - i] < now:
            check = False
            break
    for i in range(y):
        if nowi + 1 + i >= n:
            break
        if arr[nowi + 1 + i] < now:
            check = False
            break
    if check:
        print(nowi + 1)
        break
