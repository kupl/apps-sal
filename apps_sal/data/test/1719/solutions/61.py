"""
AtCoder Beginner Contest 122  D - We Like AGC

愚直解
・N文字のうち、各文字についてA,C,G,Tの4通りを取りうるので、4^N
・できた文字について、AGCを含まないか確認：N
・隣接する2文字を一回だけ入れ替えて、AGCができないか確認：N
なので、4^N * N * N ぐらいか？後ろ二つはまとめてもいいが。
また、AAAGCでNGなのがわかっているのに、AAAGCAAを作って調べる〜みたいな重複もいけてない。
このような重複を避けるには、小さい問題からメモ化で解決するDPがよいと思う

入れ替えてAGCができる時、
GAC -> AGC か、 ACG -> AGC、　AXGC -> XAGC、　AGXC -> AGCX
なので、作っている文字列の右端から3文字がわかって入れば行けそう


dp[i+1][j(i-2文字目)][k(i-1文字目)][l(i文字目)]：i文字目をl、一個手前をk、もう一個手前をjとした時の文字列の個数
とすると

遷移
・dp[i+1][A][G][C], dp[i+1][G][A][C], dp[i+1][A][C][G] :こいつらは作ってはいけない
・dp[i][A][＊][G] -> dp[i+1][*][G][C] : Aと* を入れ替えるとAGCができるのでNG
・dp[i][A][G][*] -> dp[i+1][G][*][C] : *とCを入れ替えるとAGCになるのでだめ

上の遷移はなんかややこしいので、ざっくりまとめると、　・・・pqrs　と並んでいて、pqrsについて、
A,G,*,C
A,*,G,C
*,A,G,C,
*,G,A,C
*,A,C,G
がアウトで他はOK
これをDPでやるとよい

最後に末尾3文字について、全パターン見て足し合わせる。


"""

N = int(input())
MOD = 10**9 + 7

# dp[i+1][j(i-2文字目)][k(i-1文字目)][l(i文字目)]：i文字目をl、一個手前をk、もう一個手前をjとした時の文字列の個数
# j,k,lについて、A=1,C=2,G=3,T=4, 初期化の都合上0もある
dp = [[[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)] for _ in range(N+1)]
dp[0][0][0][0] = 1
A = 1
C = 2
G = 3
T = 4

for i in range(N):
    # 初期値をうまく利用したいので、p,q,rは0~4まで
    for p in range(5):
        for q in range(5):
            for r in range(5):
                # sをA,C,G,Tで動かす
                for s in range(1, 5):
                    # ・・・・・pqrsの並びにできるか考える
                    """
                    A,G,*,C
                    A,*,G,C
                    *,A,G,C,
                    *,G,A,C
                    *,A,C,G
                    がアウト
                    """
                    if p == A and q == G and s == C : continue
                    if p == A and r == G and s == C : continue
                    if q == A and r == G and s == C : continue
                    if q == G and r == A and s == C : continue
                    if q == A and r == C and s == G : continue

                    dp[i+1][q][r][s] += dp[i][p][q][r]
                    dp[i+1][q][r][s] %= MOD


ans = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            #print(i,j,k, dp[-1][i][j][k])
            ans += dp[-1][i][j][k]
            ans %= MOD


print(ans) 

