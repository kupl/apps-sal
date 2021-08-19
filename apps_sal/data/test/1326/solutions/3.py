N = int(input())
ans = 0
for i in range(1, N + 1):
    j = N // i
    ans += i * j * (j + 1) // 2
print(ans)
