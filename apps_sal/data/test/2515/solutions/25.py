# クエリにO(1)で返すためのテーブルを用意
import numpy as np
MAX = int(10e5 + 1)
List = list(range(2, MAX))
P = []
while len(List) > 0:
    p = List[0]
    if p >= np.sqrt(MAX): break
    P.append(p)
    List = [x for x in List if x % p != 0]
P = set(P + List)

Ans = [0] * MAX
cnt = 0
for i in range(1, MAX):
    if i in P and (i + 1) // 2 in P:
        cnt += 1
    Ans[i] = cnt

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(Ans[r] - Ans[l - 1])
