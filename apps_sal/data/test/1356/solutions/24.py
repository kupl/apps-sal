s = input()
ct = 0
for i in s:
    if i == 'a':
        ct += 1
l = len(s)
ans = min(l, 2 * ct - 1)
print(ans)
