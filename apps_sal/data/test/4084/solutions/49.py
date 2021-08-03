# 入力を取得する
N, A, B = list(map(int, input().split()))

# A+B が Nの中に何セットあるかを取得
sets = N // (A + B)

# A * セット数を取得
a_count = A * sets

# NをA+Bで割った余りがAより小さければ余りを大きければAを足す
mod = N % (A + B)
a_count += mod if mod < A else A

print(a_count)
