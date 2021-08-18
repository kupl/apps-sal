n = int(input())
cnt = 0
i = 0
ans = 0
while n != 1:
    n //= 2
    i += 1

ans = 2**(i + 1) - 1


print(ans)
