
def resolve():
    # 後手必勝になる移動個数の最小を求める
    # 移動して A1xorA2 == A3~AN xor になるか
    # 移動個数を1つずつ試すとTLE なのでA1+A2を2つに分けて条件を満たす方法を探す
    N = int(input())
    A = list(map(int, input().split()))

    # A1 + A2
    S = A[0] + A[1]

    # 3～N番目のxor
    xor = 0
    for a in A[2:]:
        xor ^= a

    # S == A1xorA2 + 2(A1&A2) -> 2(A1&A2) == S - A3~AN xor
    # 2で割れなければ不可能
    S -= xor
    if S%2 == 1:
        return print(-1)

    S //= 2
    # A1&A2 と A1xorA2が同じ箇所のビットが立っていたら不可能
    if (S&xor) != 0 or S > A[0]:
        return print(-1)

    # A1 に残す個数は最低A1&A2であり、A1xorA2を上の桁から貪欲に、
    # i桁目が1かつ、減らす個数に加えてもAi以上にならないように加えていく
    b = S
    for i in range(41, -1, -1):
        if xor>>i & 1 == 1:
            if b + (1<<i) <= A[0]:
                b += 1<<i

    if b == 0:
        print(-1)
    else:
        print(A[0] - b)


def __starting_point():
    resolve()
__starting_point()
