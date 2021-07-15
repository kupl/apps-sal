n = int(input())
k = int(input())
ans = 1
for _ in range(n):
    if ans * 2 > ans + k:
        ans += k
    else:
        ans *= 2
print(ans)
