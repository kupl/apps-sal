x = int(input())
shou = x // 11
amari = x % 11
if amari == 0:
    print(shou * 2)
elif amari < 7:
    print(shou * 2 + 1)
else:
    print(shou * 2 + 2)
