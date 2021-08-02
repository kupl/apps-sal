# A Buttons
a, b = list(map(int, input().split()))
coin = 0
for i in range(2):
    if a > b:
        coin += a
        a = a - 1
    else:
        coin += b
        b = b - 1
print(coin)
