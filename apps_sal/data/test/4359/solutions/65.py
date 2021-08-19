from decimal import Decimal, ROUND_UP
l = [int(input()) for i in range(5)]
rl = []
for i in range(len(l)):
    rl.append(int(Decimal(str(l[i])).quantize(Decimal('1E1'), rounding=ROUND_UP)))
ans = []
for j in range(len(rl)):
    num = sum(rl) - rl[j] + l[j]
    ans.append(num)
print(min(ans))
