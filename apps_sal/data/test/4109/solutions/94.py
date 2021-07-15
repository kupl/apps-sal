[N, M, X] = list(map(int, list(input().split(' '))))
A = []
C = []
for i in range(N):
    c, *a = list(map(int, input().split(' ')))
    C.append(c)
    A.append(a)
#print(C)
#print(A)

INF = 10**10
min_cost = INF

for b in range(2**N): 
    # これがバイナリーベースの全探索となる。今回のキモ part 1
    # 一つのループが本の購入セットに対応している
    # 各ビットがそれぞれの本を購入するかどうか表している
    # 因みに b は bit を表しているつもり
    cost = 0 # この購入セットで使う金額
    algo_level = [0] * M # 各アルゴリズムトピックの理解度
    for i in range(N): 
        # これが各本のコストと理解度取得のためのループ
        # i 番目の本に対してループを回していく
        if(b >> i & 1): # この行が今回のキモ part 2。
            # i 番目の本の購入有無を判定するために、ビットシフトした値に対して '1 = 0b1' (つまり単なる (2進数の) 1) との論理積を求めている
            # この if 文が True であるということは、i 番目の本を買ったということ
            cost += C[i]
            for a in range(M): # (各本にある) 各アルゴリズムに対するループ
                algo_level[a] += A[i][a]
    if(min(algo_level) >= X): # 全てのアルゴリズムトピックが X 以上の理解度である場合…
        min_cost = min(cost, min_cost)

if(min_cost < INF):
    print(min_cost)
else:
    print('-1')





