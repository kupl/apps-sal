n = int(input())
s = input()
nn = len(s)
ans = 0
for i in range(n, nn, n):
    if s[i - 1] + s[i - 2] + s[i - 3] == 'aaa' or s[i - 1] + s[i - 2] + s[i - 3] == 'bbb':
        ans += 1
print(ans)
