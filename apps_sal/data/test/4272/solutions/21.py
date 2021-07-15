import re
n = int(input())
s = input()
a = []
ans = 0
for i in range(n):
    if s[i] == 'A':
        a.append(i)
for i in a:
    if s[i:i+3] == 'ABC':
        ans += 1
print(ans)
