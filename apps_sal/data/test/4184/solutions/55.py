"""
    1 から N の番号がついた N 個の重りがあり、番号 i の重りの重さは Wi です。

    ある整数 1 ≤ T < N に対してこれらの重りを、番号が T 以下の重り と
    番号が T より大きい重りの 2 グループに分けることを考え、
    それぞれのグループの重さの和を S1, S2 とします。

    このような分け方全てを考えた時、S1 と S2 の差の絶対値の最小値を求めてください。
"""
'\n制約：\n    2 ≤ N ≤ 100\n    1 ≤ Wi ≤ 100\n    入力は全て整数である\n'


def abc129b(n: int, w_lists: int) -> int:
    ret = max(w_lists)
    for i in range(n):
        temp = abs(sum(w_lists[:i]) - sum(w_lists[i:]))
        if temp < ret:
            ret = temp
    return ret


n = int(input())
w_lists = list(map(int, input().split()))
print(abc129b(n, w_lists))
