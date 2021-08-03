total = int(input())  # 宿泊日数
disc = int(input())  # 初めの割引なし日数
priceX = int(input())  # 割引ない値段
priceY = int(input())  # 割引後の値段

ans = ()
if total <= disc:
    ans = total * priceX
else:
    ans = disc * priceX + (total - disc) * priceY
print(ans)
