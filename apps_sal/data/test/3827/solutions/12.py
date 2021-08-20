s = str(input())
a = 0
b = 0
c = 0
stage = 0
for i in range(len(s)):
    if s[i] == 'a' and stage <= 1:
        a += 1
        stage = 1
    elif s[i] == 'b' and stage > 0 and (stage < 3):
        b += 1
        stage = 2
    elif s[i] == 'c' and stage > 1 and (stage < 4):
        c += 1
        stage = 3
    else:
        stage = 100
        break
if stage == 3 and a > 0 and (b > 0) and (c == a or c == b):
    print('YES')
else:
    print('NO')
