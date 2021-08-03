n, k = map(int, input().split())
s = list(input())
lr = 0
rl = 0
ans = 0
for i in range(n - 1):
    if s[i] == 'L' and s[i + 1] == 'R':
        lr += 1
    elif s[i] == 'R' and s[i + 1] == 'L':
        rl += 1
    else:
        ans += 1

if lr >= k and rl >= k:
    ans += 2 * k
elif lr == rl:
    ans += 2 * lr
else:
    num = max(lr, rl)
    ans += 2 * num - 1

print(ans)
