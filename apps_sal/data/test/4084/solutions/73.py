# N,A,Bを受け取る
N, A, B = list(map(int, input().split()))

# NをA+Bで割った商をxとし、余をyとする
x = N // (A + B)
y = N % (A + B)

# yがAより大きいかどうかで場合わけをする
print((A * x + A if y >= A else A * x + y))
