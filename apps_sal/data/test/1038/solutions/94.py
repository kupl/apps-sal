(a, b) = list(map(int, input().split()))
'\nbit ごとにみる\nb-a = even and a%2 == 0 => 1\nelse: 0\n\n（0 ~ b madeno 個数）－\u3000（0 ~ a-1 madeno 個数）\n1の位は (b+1)/2\n10の位は (b+1)/4 + max((b+1)%4-2,0)\n100の位\n'
ans = 0
if b % 2 == 1:
    ans = (b + 1) // 2 % 2
else:
    ans = b ^ b // 2 % 2
if a == 0:
    print(ans)
else:
    tmp = 0
    if (a - 1) % 2 == 1:
        tmp = a // 2 % 2
    else:
        tmp = a - 1 ^ (a - 1) // 2 % 2
    ans = ans ^ tmp
    print(ans)
