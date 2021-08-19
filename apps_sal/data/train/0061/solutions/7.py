for kek in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    flag = False
    ans = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] and p[i] > p[i + 1]:
            flag = True
            ans = i + 1
            break
    if flag:
        print('YES')
        print(ans - 1, ans, ans + 1)
    else:
        print('NO')
