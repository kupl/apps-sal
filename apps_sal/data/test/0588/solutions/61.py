import numpy as np

n = int(input())
x,y = np.array([list(map(int,input().split())) for _ in range(n)]).T

# 内積が0以上かどうか
def isin90deg(v1, v2):
    if np.dot(v1, v2) >= 0 : return 1
    else: return 0

# 内積が0かどうか
def is90deg(v1, v2):
    if np.dot(v1, v2) == 0 : return 1
    else: return 0

ans = []
for i in range(n):
    # tangent-vector, normal-vector
    tv, nv1 = np.array([x[i],y[i]]), np.array([y[i],-x[i]])
    nv2 = - nv1
    # tvから時計回り180度エリアにおけるベクトル和を考える
    # ただし、tvに平行なベクトル群（posi/nega）だけ例外処理
    for nv in [nv1, nv2]:
        sum,posi,nega = np.array([0,0]), np.array([0,0]), np.array([0,0])
        for j in range(n):
            v = np.array([x[j],y[j]])
            if isin90deg(v,nv): sum += v
            if is90deg(v,nv) and isin90deg(v,tv): posi += v
            if is90deg(v,nv) and not isin90deg(v,tv): nega += v
        # ユークリッド距離
        ans.append(np.linalg.norm(sum, ord=2))
        ans.append(np.linalg.norm(sum - posi, ord=2))
        ans.append(np.linalg.norm(sum - nega, ord=2))

print((max(ans)))



