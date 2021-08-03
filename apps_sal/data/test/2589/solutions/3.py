for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    m = sum(arr) % x
    if m != 0:
        print(n)
        continue
    ls = 0
    li = -1
    for i in range(n):
        ls += arr[i]
        li = i + 1
        if ls % x != 0:
            break
    rs = 0
    ri = -1
    for i in range(n - 1, -1, -1):
        rs += arr[i]
        ri = i
        if rs % x != 0:
            break

    if n - min(n - ri, li) == 0:
        print(-1)
    else:
        print(n - min(n - ri, li))
