N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
arm = [list(map(int, input().split())) for j in range(N)]

ans = -9999999999
for item in range(1, 2**10):
    fund = 0
    for i in range(N):
        cou = 0
        for x in range(10):
            if (item >> x) % 2 == 1 and arr[i][x] == 1:
                cou += 1
        fund += arm[i][cou]
    ans = max(ans, fund)

print(ans)
