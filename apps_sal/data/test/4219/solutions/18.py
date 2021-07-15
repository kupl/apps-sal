# 不親切な人の証言は、正しかろうが間違っていようが検証できないので無視する
# bit全探索で正直者を仮定・固定して、証言に矛盾が出なければ人数を数えて記録する
from itertools import product
n = int(input())
Ev = [[] for _ in range(n)]

for i in range(n):
    A = int(input())
    for a in range(A):
        x, y = map(int, input().split())
        Ev[i].append((x - 1, y))

bit = list(product([1, 0], repeat=n))

ans = 0
for b in bit:
    for i, v in enumerate(b):  # v == 1 or 0
        if v == 1:
            for x, y in Ev[i]:  # 証言１つ１つを取り出して検証
                if b[x] != y:  # bitで仮定している正直者リストと矛盾する証言を正直者が行ったらアウト
                    break
            else:
                continue
            break
    else:
        ans = max(b.count(1), ans)

print(ans)
