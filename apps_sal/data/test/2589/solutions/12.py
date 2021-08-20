for test_i in range(int(input())):
    (n, x) = map(int, input().split())
    arr = list(map(int, input().split()))
    if sum(arr) % x != 0:
        print(n)
    else:
        il = 1
        while il < n + 1:
            if arr[il - 1] % x > 0:
                break
            il += 1
        ir = 1
        while ir < n + 1:
            if arr[-ir] % x > 0:
                break
            ir += 1
        print(n - min(il, ir))
