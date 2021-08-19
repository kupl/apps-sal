import numpy as np

L = int(input())

branches = []
# ノード数は (2^n - 1) のときに 1 増える
node_count = int(np.log2(L)) + 1

# (0, 1), (0, 2), (0, 4), ... って2個ずつブランチ引く。
# これで 0 から 2^n - 1 (< L) まで作れる
for n in range(node_count - 1):
    branches.append((n, n + 1, 0))
    branches.append((n, n + 1, 2 ** n))

# これが '1' のノードから最後まで線を引きたい
byte_list = list(reversed(format(L, 'b')))[:-1]
# 長さはそれっぽい感じにする
a = 2 ** (node_count - 1)
for i in reversed(list(range(len(byte_list)))):
    if byte_list[i] == '1':
        branches.append((i, node_count - 1, a))
        a += 2 ** i

print((node_count, len(branches)))
for u, v, w in branches:
    print((u + 1, v + 1, w))
