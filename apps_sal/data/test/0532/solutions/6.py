s = input()
x = 'abcdefghijklmnopqrstuvwxyz'
cur = 'a'
ans = 0
for c in s:
    p = abs(x.find(cur) - x.find(c))
    p = min(p, 26 - p)
    ans += p
    cur = c
print(ans)
