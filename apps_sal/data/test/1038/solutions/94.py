a, b = list(map(int, input().split()))
"""
bit ごとにみる
b-a = even and a%2 == 0 => 1
else: 0

（0 ~ b madeno 個数）－　（0 ~ a-1 madeno 個数）
1の位は (b+1)/2
10の位は (b+1)/4 + max((b+1)%4-2,0)
100の位
"""

ans = 0
if b % 2 == 1:
    ans = (b + 1) // 2 % 2
else:
    ans = b ^ (b // 2 % 2)

if a == 0:
    print(ans)
else:
    tmp = 0
    if (a - 1) % 2 == 1:
        tmp = a // 2 % 2
    else:
        tmp = (a - 1) ^ ((a - 1) // 2 % 2)
    ans = ans ^ tmp
    print(ans)
