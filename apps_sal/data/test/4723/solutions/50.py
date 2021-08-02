import sys
import math
import re

# https://atcoder.jp/contests/agc008/submissions/15248942
sys.setrecursionlimit(10 ** 8)
ini = lambda: int(sys.stdin.readline())
inm = lambda: map(int, sys.stdin.readline().split())
inl = lambda: list(inm())
ins = lambda: sys.stdin.readline().rstrip()
debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

s2 = input()
t = input()

# 辞書順の小さいものを作るためにパターンマッチは後ろから実施したい
# ので入力を反転させる
s2_r = s2[::-1]
t_r = t[::-1]

ans_flag = False
# 全文字の組み合わせを試す
for i in range(len(s2)):
    for j in range(i + 1, len(s2) + 1):
        # tと同じ文字数の時だけ部分一致するか判定する
        if (j - i) == len(t_r):
            flag = True
            # 一文字ごとに判定する
            for k, l in enumerate(range(i, j)):
                if s2_r[l] != t_r[k] and s2_r[l] != '?':
                    flag = False
            if flag == True:
                # 一致した位置を置換
                ans = s2_r[:i] + t_r + s2_r[j:]
                # 残りの?を辞書順最小のaに置換
                ans = ans.replace('?', 'a')
                # 元の順番に反転
                ans = ans[::-1]
                print(ans)
                ans_flag = True
                break

    # forをbreakしないとcontinueする
    else:
        continue
    break

if ans_flag == False:
    print('UNRESTORABLE')
