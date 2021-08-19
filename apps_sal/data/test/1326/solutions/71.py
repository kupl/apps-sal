N = int(input())
ans = 0
for i in range(1, N + 1):
    num = N // i
    ans += i * (num * (num + 1)) // 2
print(ans)
