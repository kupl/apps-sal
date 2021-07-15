def dsf(i,sum,count,nokori):
    nonlocal ans
    # 階層が最下層になった時
    if i == d:
        #sumは絶対答えではない
        if sum < g:
            use = max(nokori)
            n = min(pc[use - 1][0],-(-(g - sum) // (100 * use)))
            count += n
            sum += n * use * 100



        # sumは答えになる可能性あり
        if sum >= g:
            ans = min(ans,count)
    else:
        #問題を解かないパターン
        dsf(i+1,sum,count,nokori)
        #問題を解くパターン(階層、合計+最大のボーナス、現在の合計の数+最大の数、残りの問題を管理)
        dsf(i + 1,sum + pc[i][0] * (i + 1) * 100 + pc[i][1],count + pc[i][0],nokori - {i + 1})
# 解く問題ととかない問題
d,g = map(int,input().split())
pc = [list(map(int,input().split())) for i in range(d)]
ans = float('inf')

#階層、合計、現在の合計の数、残りの問題を管理
dsf(0,0,0,set(range(1,d + 1)))
print(ans)
