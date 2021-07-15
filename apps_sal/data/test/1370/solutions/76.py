import numpy as np
import itertools

H, W, K = map(int, input().split())
choco = []
for i in range(H):
    choco.append([int(x) for x in list(input())])

arr = np.array(choco)

# W方向にGREEDY
count = (H-1) + (W-1)


for k in range(H):
    
    # この時点で同じ回数以上切ることが確定なら終了
    if count <= k:
        break

    # H 方向に切り込み
    for comb in itertools.combinations(range(1,H),k):

        # スライスを作っておく
        t = (None,) + comb + (None,)
        s = [slice(t[j],t[j+1],) for j in range(len(t)-1)]
        
        sum_p = [0] * (k+1)
        
        cut = k
        
        for col in zip(*choco):

            # 各ブロック毎の合計を算出
            sum_a = [sum(col[b]) for b in s]
            
            # K を超えるブロックが存在していないか？
            if any(map(K.__lt__, sum_a)):
                # 不成立
                break
            
            # 前まで分割されていないブロックと合わせて、合計を算出
            
            sum_b = [x + y for x,y in zip(sum_p, sum_a)]

            if any(map(K.__lt__, sum_b)):
                cut += 1
                sum_p = sum_a
            else:
                sum_p = sum_b
                
                # 割った位置を記録
        
        else:
            count = min(count,cut)

print(count)
