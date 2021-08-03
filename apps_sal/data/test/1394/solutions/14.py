s = input()
s1 = ''
a = 0
for i in s:
    if i != 'a':
        s1 += i
    else:
        a += 1

if len(s1) % 2 != 0:
    print(':(')
else:
    s1 = s1[:len(s1) // 2]
    N = len(s)
    n = len(s1)
    if s[N - n:] == s1:
        print(s[:N - n])
    else:
        print(':(')
