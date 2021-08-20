n = int(input())
counter = [0] * (n + 1)
for i in range(2, n + 1):
    num = i
    j = 2
    while j * j <= num:
        cnt = 0
        while num % j == 0:
            counter[j] += 1
            num //= j
        j += 1
    if num != 1:
        counter[num] += 1
ans = 1
for i in range(n + 1):
    if counter[i] > 0:
        ans *= counter[i] + 1
        ans %= int(1000000000.0 + 7)
print(ans)
