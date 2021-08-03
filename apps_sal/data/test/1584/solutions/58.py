# 小さいのを2つ選んで最後の1つをにぶたん
# なぜかTLEなる
from bisect import bisect_left
n = int(input())
l = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        # ok, ng = j, n
        # while (ng - ok) > 1:
        #     mid = (ng + ok) // 2
        #     if l[i] + l[j] > l[mid]:
        #         ok = mid
        #     else:
        #         ng = mid
        # ans += ok - j
        # ↑とやってることは同じはずなんだけどなぜかTLEなるので組み込みのやつを使ってみる
        a = bisect_left(l, l[i] + l[j])
        ans += a - 1 - j
print(ans)
