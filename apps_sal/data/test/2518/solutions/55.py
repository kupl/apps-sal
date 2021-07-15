import math
n, a, b = list(map(int, input().split()))
h_list = [int(input()) for _ in range(n)]

lb = 0
ub = 10**9 # これだけ唱えれば確実に全滅する

def is_ok(m):
    # m回の攻撃でモンスターが全滅するか
    tmp_ans = 0
    for h in h_list:
        tmp_h = max(h-m*b, 0) # モンスターの残り体力
        tmp_ans += math.ceil(tmp_h/(a-b)) # 爆発の中心になる回数
    if tmp_ans <= m:
        return True
    else:
        return False


ng = lb
ok = ub + 1
while ok - ng > 1:
    m = (ok + ng) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m

print(ok)

