def is_pal(s):
    return s == s[::-1]

s = input()
i = int(s)
j = 0
while i % 10 == 0:
    j += 1
    i /= 10

s = str(int(i))
if is_pal(s):
    print('YES')
else:
    print('NO')

