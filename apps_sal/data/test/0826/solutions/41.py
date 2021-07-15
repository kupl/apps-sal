N = int(input())

# N + 1 の丸太を、1 + 2 + 3 + .... + ok に分割する
ok = 0
ng = 10 ** 18 + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    # 1 ~ midまでの公差1の等差数列の和がN＋1以下の時はOK
    if N + 1 >= mid * (mid + 1) // 2:
        ok = mid
    else:
        ng = mid

# 1から小さい順にok本目までは、N＋1の丸太１本を分割することで得られる
# それ以外は普通に一本ずつ買う必要がある
print(N - ok + 1)
