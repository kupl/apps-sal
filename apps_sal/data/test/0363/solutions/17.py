n = int(input())
s = 9
ans = 0
i = 1
while n > 0:
    n -= s
    ans += s * i
    i += 1
    s *= 10
ans += n * (i - 1)
print(ans)
