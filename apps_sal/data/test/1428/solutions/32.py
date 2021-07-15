# D - Good Grid

from collections import defaultdict
import itertools

N, C = map(int, input().split())
D = [[0] * C for _ in range(C)]
for i in range(C):
    D[i] = list(int(d) for d in input().split())

# MOD3の世界で0,1,2ごとに、最初の値の数をカウントしておく
dict_c = [defaultdict(int) for _ in range(3)]
for i in range(N):
    c = list(int(x) for x in input().split())
    for j in range(N):
        dict_c[(i+j)%3][c[j]-1] += 1

# ここからは全探索。
# 0, 1, 2の各配列に対して、全ての色を試す(C**3)
list_C = list(range(C))
ans = 10**18
for (p, q, r) in itertools.permutations(list_C, 3):
    tmp = 0
    for i, j in enumerate((p, q, r)):
        for m, n in dict_c[i].items():
            tmp += D[m][j] * n
    ans = min(ans, tmp)

print(ans)
