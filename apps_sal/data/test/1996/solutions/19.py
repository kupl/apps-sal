n = int(input())
setr = set(chr(i) for i in range(ord('a'), ord('z') + 1))
setnr = set()
ans = 0
letter =''
isq = False
a = [input() for i in range(n)]
for s in a:
    if s[0] == '.':
        setnr = setnr | set(s[2:])
    elif s[0] == '!':
        if len(setr - setnr) == 1 or isq:
            ans += 1
        if len(setr) == 0:
            setr = set(s[2:])
        else:
            setr = setr & set(s[2:])
    elif s[0] == '?' and s[2] != a[-1][2]:
        if len(setr - setnr) == 1 or isq:
            ans += 1
        else:
            setnr.add(s[2])
    elif s[0] == '?' and s[2] == a[-1][2]:
        isq = True
print(ans)

