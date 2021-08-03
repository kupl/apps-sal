a, b, k = map(int, input().split())
taka = a - k
if taka < 0:
    aoki = b - abs(taka)
    taka = 0
    if aoki < 0:
        aoki = 0
else:
    aoki = b
print(taka, aoki)
