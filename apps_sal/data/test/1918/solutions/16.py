n = int(input())
p = [int(_) for _ in input().split()]
s = input()
ans = 0
for i in range(n):
    if s[i] == 'B':
        ans += p[i]
tmp = 0
mx = 0
for i in range(n):
    tmp += p[i] if s[i] == 'A' else -p[i]
    mx = max(tmp, mx)
tmp = 0
for i in range(n)[::-1]:
    tmp += p[i] if s[i] == 'A' else -p[i]
    mx = max(tmp, mx)
ans += mx
print(ans)
