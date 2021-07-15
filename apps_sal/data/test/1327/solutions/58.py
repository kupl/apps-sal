# 絶対値と言われたら＋とーのどっちにするのか分からない→全通りやれば良い
# 向きを固定する。
# 例えばxが+, yが-、zが+だとすると
# (x,y,z) = (3, -4, -1)の「貢献度」は3+4-1 = 6になる
# あとは貢献度の順にソートして、上位からM個を取れば良い

# L1ノルムが一定→ダイヤ型（正八面体）
# マンハッタン距離を使う問題とも通じるものがある。
# https://atcoder.jp/contests/abc178/tasks/abc178_e ABC178 E Dist Max
# 「いくつか向きの候補があるから、全通りを考えて最大を取ればいいよね。向きを固定すればあとは単純な貪欲だよね」

import copy

n, m = list(map(int, input().split()))
temp = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for x_sign in (1, -1):
    for y_sign in (1, -1):
        for z_sign in (1, -1):
            # params = temp.copy() これでは浅いコピーになるので、同じオブジェクトを指してしまう
            params = copy.deepcopy(temp)

            for xyz in params:
                xyz.append(x_sign * xyz[0] + y_sign * xyz[1] + z_sign * xyz[2])
            
            params.sort(key=lambda xyz: xyz[3], reverse=True)
            ans_sign = sum([xyz[3] for xyz in params[:m]])
            ans = max(ans, ans_sign)

print(ans)

