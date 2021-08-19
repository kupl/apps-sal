a, b = map(int, input().split())
tmp = 1  # 空き
ans = 0  # タップをさした数
while True:
    if tmp >= b:
        break
    tmp -= 1
    tmp += a
    ans += 1
print(ans)
