N = int(input())
ans = 0
for i in range(3, N + 1, 2):
    num = i
    count = 1
    for j in range(1, N // 2 + 1):
        if num % j == 0:
            count += 1
    if count == 8:
        ans += 1
print(ans)
