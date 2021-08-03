s = input()

cur = 'a'
total = 0

for k in s:
    c = abs(ord(cur) - ord(k))
    c = min(c, 26 - c)
    cur = k
    total += c

print(total)
