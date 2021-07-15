# https://atcoder.jp/contests/abc085/tasks/abc085_b
# 2分探索木を使うらしいが・・・・これは確かライブラリではなく、実装方法を気をつければ簡単に実装できた気がする。
N = int(input())
D = [int(input()) for _ in range(N)]
D.sort()
count = 1
for i in range(1, len(D)):
    if D[i] != D[i - 1]:
        count += 1
print(count)

