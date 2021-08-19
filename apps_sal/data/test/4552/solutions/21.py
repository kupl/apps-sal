n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
arm = [list(map(int, input().split())) for j in range(n)]
ans = -9999999999
for item in range(1, 1024):
    fund = 0
    for i in range(n):
        cou = 0
        for x in range(10):
            if (item >> x) % 2 == 1 and arr[i][x] == 1:
                cou += 1
        fund += arm[i][cou]
    ans = max(ans, fund)
print(ans)
