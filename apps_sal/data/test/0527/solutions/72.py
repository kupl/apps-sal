from collections import Counter
import bisect

s = input()
t = input()
"""
TLE問題なのは間違いないが、工夫も結構厳しい必要がありそう
二分探索を用いれば, O(|t| log|s|)の定数倍で解ける？
"""

# 絶対に作れないやつは-1を出す、それ以外は絶対に作れる.
sc = Counter(s)
tc = Counter(t)
for i, j in tc.most_common():
    if sc[i] == 0:
        print(-1)
        return

"""
O(|t| |s|)で解けるが、TLE確実.
bisectを使う。
"""

target = ord("a")
ordl = [[] for _ in range(26)]
for i, j in enumerate(s):
    ordl[ord(j) - target].append(i)
ordllen = [len(ordl[i]) for i in range(26)]

# ordl := 各文字のindex番号.

times = 0
cnt = -1
ans = 0
for i in t:
    k = ord(i) - target
    m = bisect.bisect_right(ordl[k], cnt)
    if m == ordllen[k]:
        times += 1
        cnt = ordl[k][0]
    else:
        cnt = ordl[k][m]

ans = times * len(s) + cnt + 1
print(ans)
