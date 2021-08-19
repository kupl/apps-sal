n = int(input())
Z = ''
sou = 'Zabcdefghijklmnopqrstuvwxyz'
N = n
for i in range(100):
    x = N % 26
    N -= x
    if x == 0:
        x = 26
        N -= x
    Z += sou[x]
    if N == 0:
        break
    N //= 26
ans = Z[::-1]
print(ans)
