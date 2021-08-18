n = int(input())
l = "Xabcdefghijklmnopqrstuvwxyz"
ans = ""
while True:
    d = n % 26
    if d == 0:
        d = 26
    ans += l[d]

    n -= d

    if n == 0:
        break

    n //= 26

print(ans[::-1])
