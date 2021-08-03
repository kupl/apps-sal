s = input()
t = input()
res = 0
for x in t:
    if s[res] == x:
        res += 1
print(res + 1)
