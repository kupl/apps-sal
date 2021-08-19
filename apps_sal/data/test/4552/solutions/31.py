N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
arm = [list(map(int, input().split())) for j in range(N)]

ans = -9999999999
for item in range(1, 2**10):  # joisinoお姉ちゃんが営業するしないの組み合わせ1024通り
    fund = 0
    for i in range(N):  # 店の数
        cou = 0
        for x in range(10):  # 営業タイミング（月~金それぞれ午前、午後）
            if (item >> x) % 2 == 1 and arr[i][x] == 1:  # joisino姉の開店と店iの開店が一致
                cou += 1
        fund += arm[i][cou]
    ans = max(ans, fund)

print(ans)
