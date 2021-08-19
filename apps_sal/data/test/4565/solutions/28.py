n = int(input())
s = input()
l = [0] * n
r = [0] * n
for i in range(1, n):
    l[i] = l[i - 1] + (s[i - 1] == 'W')
for i in range(n - 2, -1, -1):
    r[i] = r[i + 1] + (s[i + 1] == 'E')
ans = n - 1
for i in range(n):
    ans = min(ans, l[i] + r[i])
print(ans)
