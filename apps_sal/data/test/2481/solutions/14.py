"""
きょうぎぷろぐらみんぐ！！！！！！
競プロ競プロ競プロ競プロ競プロ競プローーーーー！！！！！！！
hshs！！ﾊｱﾊｱ！！興奮興奮！！！！うおおおおおおお！！！
競プロの重要性！！ｺﾞﾝｺﾞﾝｺﾞﾝｺﾞﾝ(頭を難易度の壁に打ち付ける音)
うおおおおおおお！！競プロの重要性！！
"""
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
(h, w) = list(map(int, input().split()))
num = [list(map(int, input().split())) for _ in range(10)]
num = csr_matrix(num)
ans = shortest_path(num)
ans = ans.tolist()
ans2 = [0] * 10
for i in range(10):
    ans2[i] = int(ans[i][1])
ans3 = 0
for i in range(h):
    a = list(map(int, input().split()))
    for j in range(w):
        if a[j] != -1:
            ans3 += ans2[a[j]]
print(ans3)
