n = int(input())
arr = [int(x) for x in input().split()]
if n == 1:
    print(1)
else:
    for i in 16, 8, 4, 2:
        if i > n:
            continue
        for k in range(0, n, i):
            if sorted(arr[k:k + i]) == arr[k:k + i]:
                print(i)
                return
    print(1)
    return
