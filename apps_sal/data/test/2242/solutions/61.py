from collections import Counter

# forを逆から回して下から素直にmodを取るとTLEだった
# 累積和的な計算で高速化、やりやすくするためにreverse
S = input()[::-1]
# ex. 1817181712114 → 4112171817181
# print(S)

# 0桁目までのMODを0とすることで、
# 1桁目を含む数が2019の倍数の時に都合が良くなる
X = [0]

# 4,14,114,2114,12114,...のmod2019を計算

# pow(a,b,c)は普通にMODするより速い
# 普通にやったらTLEだった
for i, s in enumerate(S):
    X.append((X[-1] + int(s) * pow(10, i, 2019)) % 2019)
# print(X)


C = Counter(X)
# print(C)

ans = 0
# Xが同じになったところを2つ選べば題意を満たす
# v_C_2の計算
for v in list(C.values()):
    ans += v * (v - 1) // 2

print(ans)
