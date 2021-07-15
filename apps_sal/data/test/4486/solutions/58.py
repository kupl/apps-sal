# B - OddString

# s
s = input()
j = 0
m = ''
for i in s:
    j += 1
    if j % 2 == 1:
        m += i

print(m)


