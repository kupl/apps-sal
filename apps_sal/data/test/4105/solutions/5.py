(n, k) = list(map(int, input().split()))
arr1 = [i for i in range(1, k + 1)]
arr2 = arr1[1:] + [arr1[0]]
if k * (k - 1) >= n:
    print('YES')
    for i in range(k - 1):
        for j in range(k):
            print(str(arr1[j]) + ' ' + str(arr2[j]))
            n -= 1
            if n == 0:
                break
        if n == 0:
            break
        arr2 = arr2[1:] + [arr2[0]]
else:
    print('NO')
