k = int(input())
k *= 9
amari = 63
for i in range(1, 10 ** 6 + 1):
    amari %= k
    if amari == 0:
        print(i)
        break
    else:
        amari = amari * 10 + 63
else:
    print(-1)
