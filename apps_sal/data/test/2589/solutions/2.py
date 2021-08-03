for _ in range(int(input())):
    n, x = list(map(int, input().split()))
    # n = int(input())
    arr = list(map(int, input().split()))
    s = sum(arr)
    if s % x != 0:
        print(n)
        continue
    for l in range(n):
        if arr[l] % x != 0:
            break
    for r in range(n - 1, -1, -1):
        if arr[r] % x != 0:
            break
    if arr[l] % x == 0:
        print(-1)
    else:
        print(n - min(n - r - 1, l) - 1)
