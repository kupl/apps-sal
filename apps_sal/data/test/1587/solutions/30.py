n = int(input())
s = input()
r = s.count('R')
ans = 0
for i in range(r):
    if s[i] == 'W':
        ans += 1
print(ans)
