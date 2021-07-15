
from collections import Counter
def resolve():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    CNT = Counter(A)

    for i in range(M):
        b, c = list(map(int, input().split()))
        CNT[c] += b

    cards = sorted(list(CNT.items()), key=lambda x: x[0], reverse=True)

    # 0～B枚選択すれば良い（ちょうどB枚では無い）
    # 大きい値から消化していく
    ans = 0
    for key, cnt in cards:
        if N > cnt:
            ans += key * cnt
            N -= cnt
        else:
            # 残りの枚数を加える
            ans += key * N
            print(ans)
            return


def __starting_point():
    resolve()

__starting_point()
