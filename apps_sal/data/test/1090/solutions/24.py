(n, k) = list(map(int, input().split()))
s = input()
x = 0
y = 0
ans = n
for i in range(n - 1):
    if s[i:i + 2] == 'RL':
        x += 1
    if s[i:i + 2] == 'LR':
        y += 1
x = max(x - k, 0)
y = max(y - k, 0)
ans = ans - x - y - 1
print(ans)
