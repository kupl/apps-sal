N = int(input())

ans = 0

for num in range(1, N + 1):
    count = N // num

    ans += count * (count + 1) // 2 * num

print(ans)
