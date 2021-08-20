s = input()
a = 0
t = 0
for i in s:
    if i == 'a':
        a += 1
    else:
        t += 1
print(a + min(a - 1, t))
