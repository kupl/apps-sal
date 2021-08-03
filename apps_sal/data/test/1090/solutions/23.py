n, k = list(map(int, input().split()))
target = input('')
target = list(target)
ans = 0
p = 0
for i in range(1, n):
    if target[i - 1] != target[i]:
        p += 1
    else:
        ans += 1

print((ans + min(p, k * 2)))
