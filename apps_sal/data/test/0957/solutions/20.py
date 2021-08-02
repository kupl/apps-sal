s = input()
m = 'heidi'
for c in m:
    a = s.find(c)
    if a == -1:
        print('NO')
        return
    s = s[a + 1:]
#	print(a, c, m, s)
print('YES')
