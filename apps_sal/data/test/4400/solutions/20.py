s = input()
c = 0
c_max = 0
for i in s:
    if i == 'R':
        c += 1
    else:
        c_max = max(c_max, c)
        c = 0
    c_max = max(c_max, c)
print(c_max)
