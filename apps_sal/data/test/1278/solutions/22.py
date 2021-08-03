n, x, y = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    flag = True
    l = i - 1
    r = i + 1
    while l >= 0 and i - l <= x:
        if a[l] <= a[i]:
            flag = False
        l -= 1
    while r < n and r - i <= y:
        if a[r] <= a[i]:
            flag = False
        r += 1
    if flag == True:
        print(i + 1)
        return
