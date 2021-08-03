s = input()
n = len(s)

p = 0
ans = 0

for i in range(n):
    s1 = s[i]
    if s1 == 'g':
        p += 1
    else:
        p -= 1
    n -= 1
    if p >= n:
        break

for i in range(n):
    if s[-i - 1] == 'g':
        ans += 1

print(ans)
