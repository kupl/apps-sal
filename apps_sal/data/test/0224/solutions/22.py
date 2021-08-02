s = input()
s = s + 'A'
m = 0
cur = -1
while cur != len(s) - 1:
    i = cur + 1
    while s[i] not in ['A', 'E', 'Y', 'U', 'I', 'O']:
        i += 1
    m = max(m, i - cur)
    cur = i
print(m)
