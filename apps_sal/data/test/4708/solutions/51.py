total = int(input())
disc = int(input())
priceX = int(input())
priceY = int(input())

ans = ()
if total <= disc:
    ans = total * priceX
else:
    ans = disc * priceX + (total - disc) * priceY
print(ans)
