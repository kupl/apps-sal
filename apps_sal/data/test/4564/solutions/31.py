s = str(input())
chars = set()
ans = 'yes'
for c in s:
    if c in chars:
        ans = 'no'
        break
    chars.add(c)
print(ans)
