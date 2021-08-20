for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    (*arr,) = list(map(int, input().split()))
    cnt = 0
    mn = min(arr)
    arr.remove(mn)
    for v in arr:
        cnt += (k - v) // mn
    print(cnt)
