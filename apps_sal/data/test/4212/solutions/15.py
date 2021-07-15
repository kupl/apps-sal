# 参考 : https://atcoder.jp/contests/abc165/submissions/16921279
# 参考 : https://atcoder.jp/contests/abc165/submissions/16832189
from collections import deque
n,m,q = list(map(int,input().split()))
l = [list(map(int,input().split())) for i in range(q)]
a,b,c,d = [list(i) for i in zip(*l)]
# 数列 A の基(最初は1を入れておく)
queue = deque([[1]])
ans = 0
# 数列 A の候補がなくなる(キューが空になる)まで探索
while queue:
    # 数列 A を前から一つ取り出す
    x = queue.popleft()
    # 数列 A が長さ N か
    if len(x) == n:
        s = 0
        # 実際に何点取得できるか
        for i in range(q):
            if x[b[i]-1] - x[a[i]-1] == c[i]:
                s += d[i]
        ans = max(ans,s)
    else:
        # 違う場合、後ろに数字を付け足す
        # 付け足す数字は取り出した数列 A の一番後ろの値から M まで
        # 最終的に長さが 1 , 2 ... N となり、if の条件を満たすようになる
        for j in range(x[-1],m+1):
            y = x + [j]
            queue.append(y)
print(ans)
# 制約
# 2 <= N <= 10
# 1 <= M <= 50
# 1 <= Q <= 50
# なのでこの探索は間に合う
# 入力例 1 は A[1,3,4]
# 入力例 2 は A[1,1,1,4]
# 入力例 3 は A[1,1,1,1,1,1,1,1,1,10]
# が最大得点となる

