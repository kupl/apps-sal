# abc129B
# https://atcoder.jp/contests/abc129/tasks/abc129_b

# 1からNの番号のついたN個の重りがある
# 番号の重りの重さはW
# 1<T<N の重りを、番号がT以下の重りと番号がTより大きい重りの2グループに分ける
# それぞれのグループの重さの和をS1とS2とする
# S1とS2の差の絶対値の最小値をもとめる

# abs:絶対値もとめる関数
# min:最小値もとめる関数

# 入力
n = int(input())
w = list(map(int, input().split()))

# 処理
# 差を求めたものをリストに入れとく
df_list = []
for t in range(n - 1):
    # 1からTまでのグループの和
    s1 = sum(w[:t + 1])
    # TからNまでのグループの和
    s2 = sum(w[t + 1:])
    # S1とS2の差
    df_list.append(abs(s1 - s2))
    answer = min(df_list)

print(answer)
