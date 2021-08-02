x = int(input())
ans = 0
yokin = 100
while yokin < x:
    ans += 1
    yokin += yokin // 100
print(ans)
