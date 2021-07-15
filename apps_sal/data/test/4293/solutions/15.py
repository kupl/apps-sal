p,q,r = map(int, input().split())

# 飛行ルートは、p,q,r のみ。

# 結局はルートp＋r、p＋q、r＋qの内から最小のものを選ぶ
print(min([p+r, p+q, r+q]))
