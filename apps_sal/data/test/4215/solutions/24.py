# 問題：https://atcoder.jp/contests/abc143/tasks/abc143_a

a, b = list(map(int, input().strip().split()))
res = max(0, a - 2 * b)
print(res)
