s = input()
p = 0
for x in s:
    if x == 'p':
        p += 1
print(len(s) // 2 - p)
