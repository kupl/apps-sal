s = input()
length = len(s)
a = ord('a')
i = 0
for c in s:
    if a + i < ord(c):
        print('NO')
        break
    if a + i == ord(c):
        i += 1
else:
    print('YES')
