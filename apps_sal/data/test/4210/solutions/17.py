try:
    while True:
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        dic = {}
        for idx in range(n):
            l = len(str(arr[idx]))
            r = arr[idx] % k
            dic[(l, r)] = dic.get((l, r), 0) + 1
        res = 0
        for i in range(n):
            for j in range(1, 11):
                cur = arr[i] * int(pow(10, j))
                cr = cur % k
                l = len(str(arr[i]))
                r = arr[i] % k
                res += dic.get((j, (k - cr) % k), 0) - ((l, r) == (j, (k - cr) % k))
        print(res)
except Exception as e:
    pass
