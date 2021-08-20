n = int(input())
ans = 0
for x in range(1, n + 1, 2):
    i = 1
    count = 0
    while i * i <= x:
        if x % i == 0:
            count += 1
            if i != x // i:
                count += 1
        i += 1
    if count == 8:
        ans += 1
print(ans)
