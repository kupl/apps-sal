def out(l):
    i = 0
    while i + 1 < len(l):
        print(l[i], l[i + 1])
        i += 2


n = int(input())
s = input()
t = input()
ab = []
ba = []
for i in range(n):
    if s[i] == 'a' and t[i] == 'b':
        ab.append(i + 1)
    if s[i] == 'b' and t[i] == 'a':
        ba.append(i + 1)

if len(ab) % 2 == len(ba) % 2:
    cnt = len(ab) // 2 + len(ba) // 2
    if len(ab) % 2 == 1:
        cnt += 2
    print(cnt)
    out(ab)
    out(ba)
    if len(ab) % 2 == 1:
        a = ab[len(ab) - 1]
        b = ba[len(ba) - 1]
        print(a, a)
        print(a, b)
else:
    print(-1)
