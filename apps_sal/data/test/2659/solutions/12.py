"""
参考：https://nuekodory.github.io/2018/06/24/AtCoder-ABC101-ARC-099-%E3%82%92-Python3-%E3%81%A7%E8%A7%A3%E3%81%8F/
\u3000\u3000\u3000http://xxxasdfghjk999.hatenablog.jp/entry/2018/07/22/162323
\u3000\u3000\u3000http://drken1215.hatenablog.com/entry/2018/06/24/010600
\u3000\u3000\u3000http://phyllo-algo.hatenablog.com/entry/2018/06/24/160442
・事前にいくつかの範囲を調べて、候補の数がabc9999....のあたりだけだと予測しておく。
・候補の値だけに絞って最大値から下がっていく。
"""
K = int(input())


def make_snk(num):
    s = str(num)
    sm = 0
    for c in s:
        sm += int(c)
    return num / sm


snk_list = []
mn = float('inf')
suff = '999999999999'
for i in range(11):
    for j in range(999, 99, -1):
        j = int(str(j) + suff)
        num = make_snk(j)
        if num <= mn:
            snk_list.append(j)
            mn = num
    suff = suff[:-1]
for i in range(9999, 0, -1):
    num = make_snk(i)
    if num <= mn:
        snk_list.append(i)
        mn = num
snk_list.reverse()
for i in range(K):
    print(snk_list[i])
