for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    l1, r1 = list(map(int, input().split()))
    l2, r2 = list(map(int, input().split()))
    if l1 > l2:
        l1, r1, l2, r2 = l2, r2, l1, r1

    if l2 > r1:
        ans = float("inf")
        for i in range(1, n + 1):
            temp = i * (l2 - r1)
            limit = (r2 - l1) * i
            if k <= limit:
                temp += k
                ans = min(ans, temp)
            else:
                temp += limit
                K = k - limit
                temp += 2 * K
                ans = min(ans, temp)
        print(ans)
    else:
        count = n * (min(r1, r2) - l2)
        res = 0
        if count > k:
            print(res)
            continue
        b = max(r2, r1) - min(l2, l1) - (min(r1, r2) - l2)
        for i in range(n):
            if k - count <= b:
                res += k - count
                break
            else:
                res += b
                count += b
        else:
            res += (k - count) * 2
        print(res)
