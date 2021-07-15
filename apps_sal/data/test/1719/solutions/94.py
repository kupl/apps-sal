import sys
sys.setrecursionlimit(10**6)

n = int(input())
MOD = 10**9+7

dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(101)]

# ATCGは0123と読み替える
# 長さ0の文字列は1。0,1,2に関する制約しかないので、Sは333Sと考えても問題がない
dp[0][3][3][3] = 1

# 文字列の文字数
for length in range(n):
    # 最後から1文字目の文字
    for c1 in range(4):
        # 最後から2文字目の文字
        for c2 in range(4):
            # 最後から3文字目の文字
            for c3 in range(4):
                # 条件に当てはまる物がない場合はcontinue
                if dp[length][c1][c2][c3] == 0: continue
                # 新しく追加する文字
                for a in range(4):
                    
                    # ダメな5条件をカット
                    if a==2 and c1==1 and c2==0: continue
                    if a==2 and c1==0 and c2==1: continue
                    if a==1 and c1==2 and c2==0: continue
                    if a==2 and c1==1 and c3==0: continue
                    if a==2 and c2==1 and c3==0: continue
                    
                    # ダメな条件を抜けたら、aを足した文字列を作れる
                    # S = ... c3 c2 c1
                    # nextS = ... c2 c1 a
                    dp[length+1][a][c1][c2] += dp[length][c1][c2][c3]
                    dp[length+1][a][c1][c2] %= MOD
                    
ans = 0
# 最後から1文字目の文字
for c1 in range(4):
    # 最後から2文字目の文字
    for c2 in range(4):
        # 最後から3文字目の文字
        for c3 in range(4):
            # 長さnの文字列の値をまとめる
            ans += dp[n][c1][c2][c3]
            ans %= MOD
            
print(ans)
