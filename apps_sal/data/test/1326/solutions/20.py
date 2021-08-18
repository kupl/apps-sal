N = int(input())
ans = 0
for i in range(1, N + 1):
    max_i_multi = N // i
    ans += (max_i_multi * (max_i_multi + 1) * i) // 2
print(ans)
