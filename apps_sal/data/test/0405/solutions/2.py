n = int(input())
s = input()
ans = 0
for i in range(0, n):
    if s[i] == '<':
        ans += 1
    else:
        break
for i in range(n - 1, -1, -1):
    if s[i] == '>':
        ans += 1
    else:
        break
print(ans)
