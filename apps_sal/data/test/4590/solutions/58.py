from itertools import accumulate
import bisect

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_acc = [0] + list(accumulate(a))  # aを0冊読む=1冊も読まない場合があるので、[0]を先頭に追加します
b_acc = list(accumulate(b))  # bisect_rightでは、x以下の要素がいくつあるか？を求めるので、こちらに0は入れません

ans = 0
for an in range(n + 1):
    rem = k - a_acc[an]
    if rem < 0:
        # aをこれ以上読めません
        break

    bn = bisect.bisect_right(b_acc, rem)
    ans = max(ans, an + bn)

print(ans)
