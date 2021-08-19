# 問題：https://atcoder.jp/contests/abc138/tasks/abc138_b

n = int(input())
a = list(map(int, input().strip().split()))

res = 0
for i in range(n):
    res += 1 / a[i]
res = 1 / res

print(res)
