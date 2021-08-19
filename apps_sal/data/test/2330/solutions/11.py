for _ in range(int(input())):
    (n, m) = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    if m < n or n == 2:
        print(-1)
    else:
        total = 0
        ans = []
        for i in range(n):
            total += arr[i] + arr[(i + 1) % n]
            ans.append((i + 1, (i + 1) % n + 1))
        for i in range(m - n):
            total += arr[0] + arr[1]
            ans.append((1, 2))
        print(total)
        for ele in ans:
            print(*ele)
