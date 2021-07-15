n = int(input())
i = 2
ans = -1
while i * i <= n:
    if n % i == 0:
        ans = i
        break
    i += 1
print(str(ans) + str(n // ans))
