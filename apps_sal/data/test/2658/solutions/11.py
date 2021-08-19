# nは街の数　kは移動の回数　k＋１個の街にいくことになる　
# 最高でもn回移動すれば一つは二回訪れる街が現れる　そのあとはループする
n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

b = [-1] * (n + 1)  # 街３に5回目の移動でついた場合、b[3]に５が入る　
tmp = []  # 経路を記録していく
here = 1
count = 0  # 移動回数

while True:
    if b[here] != -1:  # 一度訪れた街に再び来た
        roop = count - b[here]  # ループの長さ　(街aに二回目に来た時の移動回数-一回目に来た時の移動回数)
        if k < count:  # ループに入る前に移動が終わった時
            print((tmp[k]))
        else:
            new_tmp = tmp[b[here]:]
            s = k - b[here]
            print((new_tmp[s % roop]))
        break
    b[here] = count
    count += 1
    tmp.append(here)
    here = a[here - 1]
