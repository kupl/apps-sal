N = int(input())

s = ""

while N != 0:
    # Pythonでは負の数を割っても余りが正になる
    # -2で割ったときの"理想的な"余り(0or1になってくれる)は2で割った余りと同じ
    r = int(N % 2)
    # ここは-2
    N = (N - r) / (-2)
    s += str(int(r))

# N=0の時はから文字列が返ってきてしまう
if s == "":
    print((0))
    return
else:
    # reverse
    print((s[::-1]))
