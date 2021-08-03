# 解説を読みながら自作

S = input()
T = input()

s_len = len(S)
t_len = len(T)

res = []

init_K = "?" * s_len
for i in range(s_len - t_len + 1):
    K = list(init_K[:i] + T + init_K[i + t_len:])
    # KをSにしたがって書き換えていく。書き換えられない→正解ではない
    for j in range(s_len):
        if S[j] == "?" or S[j] == K[j]:  # Sが"?"またはSとKが一致、書き換える必要なし
            pass
        elif K[j] == "?":  # Sが"?"ではなくてKが"?"、書き換える
            K[j] = S[j]
        else:  # それ以外、書き換えられない
            break
    else:  # breakしなかった
        # 辞書順で最小になるように、残ったKの"?"を"a"に変える
        res.append("".join(K).replace("?", "a"))

if res:
    res.sort()
    print((res[0]))
else:
    print("UNRESTORABLE")
