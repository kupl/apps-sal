N = int(input())
ans = 0
for i in range(1, N + 1):
    val = N // i
    ans += val * (val + 1) * i // 2
print(ans)
