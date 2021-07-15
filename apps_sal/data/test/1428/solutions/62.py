N,C = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(C)]

# 3色を保持するための変数
g0=[0]*C # 斜め列1
g1=[0]*C # 斜め列2
g2=[0]*C # 斜め列3

# 以下のような斜めごとに列を3色に分けようとしたときの違和感(コスト)を考える
# □ ○ △ □
# ○ △ □ ○
# △ □ ○ △
# □ ○ △ □

for i in range(N):
    col=list(map(int,input().split()))
    # 各マスの各色を見ていく
    #   斜めの列3種類ごとに持つ色を保持しておく
    for j in range(N):
        col[j]-=1
        if (i+j)%3==0:
            g0[col[j]]+=1
        elif (i+j)%3==1:
            g1[col[j]]+=1
        else:
            g2[col[j]]+=1

ans=float('inf')
# 全探索して、何色に変えるのが最もコストが低いかを出す
for i in range(C): # g0の色(をiにした場合)
    for j in range(C): # g1の色(をjにした場合)
        for k in range(C): # g2の色(をkにした場合)
            if i==j or j==k or i==k: # g0とg1が同じ色になる、みたいなパターンはないのでその場合の色分けは考えなくて良いので飛ばす
                continue
            s=0
            for l in range(C):
                # d[l][i]*g0[l]: lの色をiに変えるのに必要なコストの合計
                #  lをiに変えるコスト * g0にあるlの色の数
                #  d[l][j], d[l][k]も同様の計算
                #    l(全色)を特定のiやjに変えたときのコストの合計を算出
                s+=d[l][i]*g0[l]+d[l][j]*g1[l]+d[l][k]*g2[l]
            ans=min(ans,s)
print(ans)
