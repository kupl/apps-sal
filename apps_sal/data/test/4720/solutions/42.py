# 入力
N = int(input())

sm = 0

for i in range(N):
    l, r = map(int, input().split())
    sm += r - l + 1

# 出力
print(sm)
