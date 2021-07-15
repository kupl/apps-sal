
from itertools import accumulate
from collections import defaultdict, deque
def resolve():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A = accumulate([a % K for a in A])
    A = [0] + list(A)

    # 区間 [i,j] の和(累積和): dj+1−di
    # 区間 [i,j] の要素の数(0_indの為 +1): j−i+1
    # 上記を一般化:  dr−dl=r−l となるものの個数を求める
    # r−l<K  の時、mod K において式変形が成り立つ, dr−r=dl−l
    # rを固定し辞書で管理すれば、dl−lと同じ値なので個数を求められる。

    cnt = defaultdict(int)
    q = deque()
    ans = 0
    for r in range(N + 1):
        t = (A[r] - r) % K
        ans += cnt[t]
        cnt[t] += 1

        q.append(t)
        if len(q) == K:
            left = q.popleft()
            cnt[left] -= 1

    print(ans)


def __starting_point():
    resolve()

__starting_point()
