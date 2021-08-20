n = int(input())
ans = ''
for i in range(1, 99):
    if n <= 26 ** i:
        n -= 1
        for j in range(i):
            ans += chr(ord('a') + n % 26)
            n //= 26
        break
    else:
        n -= 26 ** i
print(ans[::-1])
