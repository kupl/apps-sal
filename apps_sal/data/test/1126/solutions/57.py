#繰り返しを探す
N,X,M = list(map(int, input().split()))

#ループ前　ループ中　ループ後　の合計をそれぞれ求め、その和を求める
pre_loop_sum = 0
all_loop_sum = 0
incomplete_loop_sum = 0

loop_flag = False

L = []
L.append(X  % M)

#高速化のため
S = set()

#繰り返しが起きるまでの配列の作成
for i in range(1,N):
    X = pow(X,2,M)

    if X in S:
        loop_flag = True
        break
    else:
        L.append(X)
        S.add(X)

index = L.index(X)

len_L = len(L)

if loop_flag:
    #繰り返しが発生した場合
    #ループ前の合計を取得
    pre_loop_sum = sum(L[0:index])

    #ループ内の合計値、ループの長さ、ループの発生回数の取得
    loop_sum = sum(L[index:len_L])
    loop_len = len_L - index
    loop_count = (N - index) // loop_len

    #ループ中の合計を取得
    all_loop_sum = loop_count * loop_sum

    #ループ仕切れない余り部分の取得
    incomplete_loop_len = (N - index) % loop_len
    incomplete_loop_sum = sum(L[index:index+incomplete_loop_len])
else:
    #繰り返しが発生しない場合
    pre_loop_sum = sum(L)

ans = pre_loop_sum + all_loop_sum + incomplete_loop_sum

print(ans)

