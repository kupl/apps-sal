(n, k) = (int(input()) for i in range(0, 2))
ans = 1
for i in range(0, n):
    if ans * 2 <= ans + k:
        ans *= 2
    else:
        ans += k
print(ans)
