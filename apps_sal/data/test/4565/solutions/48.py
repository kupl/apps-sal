from collections import Counter
n = int(input())
s = input()
sn = Counter(s)

l = 0
r = sn['E']

ans = r
for i in range(n):
    if s[i] == 'W':
        l += 1
    else:
        r -= 1
    ans = min(ans, l+r)
print(ans)

