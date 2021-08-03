def count_devisor(n):
    i = 1
    count = 0
    while i * i <= n:
        if n % i == 0:
            count += 2
        i += 1
    return count


n = int(input())
ans = 0

for i in range(1, n + 1, 2):
    if count_devisor(i) == 8:
        ans += 1
print(ans)
