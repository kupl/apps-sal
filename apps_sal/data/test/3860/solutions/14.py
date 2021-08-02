b = int(input())
g = int(input())
n = int(input())
ans = 0
for i in range(n + 1):
    if i > b:
        continue
    if n - i > g:
        continue
    ans += 1

print(ans)
