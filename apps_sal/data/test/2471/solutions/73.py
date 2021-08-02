from collections import defaultdict
import sys
readline = sys.stdin.readline

H, W, N = list(map(int, readline().split()))

# 9x9のマスの左上のマスの座標をキーにして、各正方形の黒マス数をdictionaryで管理
# 10 ** 5 * 9程度

dic = defaultdict(int)

for i in range(N):
    a, b = list(map(int, readline().split()))
    a, b = a - 1, b - 1
    for A in range(max(0, a - 2), min(a + 1, H - 2)):
        for B in range(max(0, b - 2), min(b + 1, W - 2)):
            dic[(A, B)] += 1

ans = [0] * 10
for v in list(dic.values()):
    ans[v] += 1

ans[0] = (H - 2) * (W - 2) - sum(ans[1:])

for a in ans:
    print(a)
