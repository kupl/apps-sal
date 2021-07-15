import sys

n = int(input())

# 奇数始まりは必ず0
if n % 2 == 1:
    print(0)
    return

# 5の因子を数える
# 5の倍数は10個ごと、25の倍数は50個ごと、125の倍数は250個ごとに登場する
ans = 0
cnt = 1
while 5**cnt * 2 <= n:
    ans += n // (5**cnt * 2)
    cnt += 1
print(ans)
