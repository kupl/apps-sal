# 初期入力
import sys
input = sys.stdin.readline  # 文字列では使わない

N, M = map(int, input().split())
ans = 1
ab = [0] * M
for i in range(M):
    a, b = map(int, input().split())  # 争いのある部分
    ab[i] = (a, b)

# abをbでソート
ab.sort(key=lambda x: x[1], reverse=True)
max_a = ab[0][0]
for a, b in ab:
    if max_a < b:
        max_a = max(max_a, a)
        continue
    else:
        max_a = a
        ans += 1
print(ans)
