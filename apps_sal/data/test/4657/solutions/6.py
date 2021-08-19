from sys import stdin
q = int(stdin.readline())
for i in range(q):
    (n, k) = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))
    count = 0
    ans = []
    s = 0
    for i in range(n):
        if count != k - 1:
            if arr[i] % 2 != 0:
                ans.append(i + 1)
                count += 1
                s = 0
            else:
                s += arr[i]
        else:
            if sum(arr[i:]) % 2 != 0:
                ans.append(n)
            else:
                pass
            break
    if len(ans) != k:
        print('NO')
    else:
        print('YES')
        for i in range(k - 1):
            print(ans[i], end=' ')
        print(ans[-1])
