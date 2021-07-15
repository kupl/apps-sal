n = int(input(''))
ans = 0
i = 0
lst = [4, 1, 3, 2, 0, 5]
while n > 0:
    ans += (n % 2) * 2 ** lst[i]
    i += 1
    n //=2
print(ans)
