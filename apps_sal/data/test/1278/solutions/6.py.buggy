n, x, y = list(map(int, input().split()))
a = list(map(int, input().split()))
for i in range(n):
    k = a[i]
    for j in range(max(0, i - x), min(i + y + 1, n)):
        if j == i:
            continue
        if a[j] <= k:
            break
    else:
        print(i + 1)
        return
