s = input()
f = 0
for i in range(1, len(s)):
    sl = s[0:i]
    for j in range(0, i):
        if sl == s[j:len(s)]:
            print('YES')
            print(sl)
            f = 1
            break
    if f == 1:
        break
if f == 0:
    print('NO')
