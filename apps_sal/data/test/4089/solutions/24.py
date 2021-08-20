n = int(input())
b = 26
ans = []
for i in range(1, 99):
    if n <= b ** i:
        n -= 1
        for j in range(i):
            ans.append(chr(97 + n % b))
            n //= b
        break
    else:
        n -= b ** i
for k in range(1, len(ans) + 1):
    print(ans[-k], end='')
