(n, m) = map(int, input().split())
for i in range(n):
    k = input()
f = 1
ans = 0
for i in k:
    if i == 'B' and f:
        ans += 1
        f = 0
    if i == '.':
        f = 1
print(ans)
