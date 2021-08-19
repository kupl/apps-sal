import decimal
(a, b) = list(map(int, input().split()))
num = decimal.Decimal((a + b) / 2)
ans = int(num)
if num % 1 != 0:
    ans += 1
print(ans)
