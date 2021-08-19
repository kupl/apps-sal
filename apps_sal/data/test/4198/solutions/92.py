# https://atcoder.jp/contests/abc146/tasks/abc146_c
# 二部探索

a, b, x = map(int, input().split())
i = 1
low = 0
high = 10**9 + 1
while low <= high and i <= 100:
    mid = (low + high) // 2
    if (a * mid + b * len(str(mid))) > x:
        high = mid
    else:
        low = mid
    i += 1
print(low)
