
"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc098/tasks/arc098_c

Nの制約が小さい→O(N**2) ?

小さい方からQこの集合にするのは簡単→最小を含むように範囲を選んでけば良い
重要なのは最小の奴を飛ばして範囲がちぢめられるとき。

→最小値を全探索するのか？

最小値を決め、それ以下の数字を含まないようにできるだけ小さい方からとっていく？

k以下の数字のindexで配列を切る。O(N)
各数字がどこに属しているかを二分探索で小さい方からとっていく？
O(NlogN)

→O(N**2logN)で解ける(ちょっときつくないですか)
各数字が領域差しておくか前処理して置けばO(N**2)で解けるかな

"""

N, K, Q = list(map(int, input().split()))
a = list(map(int, input().split()))

ai = []
for i in range(N):
    ai.append([a[i], i])
ai.sort()

ans = ai[Q - 1][0] - ai[0][0]

for cant in range(N - Q):

    # 0 ~ cantまでのai[i]を取ってはいけない

    rannum = [-1] * (cant + 2)
    rannum[0] = 0
    indlis = [0] * N  # rannumのindexを指し示す

    for i in range(cant + 1):

        na, nind = ai[i]
        indlis[nind] += 1

    for i in range(N):

        if i != N - 1:
            indlis[i + 1] += indlis[i]

        rannum[indlis[i]] += 1

    #print (rannum , indlis)

    ncat = []
    for i in range(cant + 1, N):

        na, nind = ai[i]

        if rannum[indlis[nind]] >= K:
            ncat.append(na)
            rannum[indlis[nind]] -= 1

        if len(ncat) == Q:
            ans = min(ans, ncat[-1] - ncat[0])
            break

    #print (ncat)

print(ans)
