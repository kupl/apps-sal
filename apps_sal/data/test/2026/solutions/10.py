n = int(input())
(*s,) = list(map(lambda x: 'URDL'.find(x), list(input())))
last = set()
cnt = 0
for i in range(len(s)):
    d = s[i]
    for ld in last:
        if min(abs(ld - d), 4 - abs(ld - d)) > 1:
            cnt += 1
            last = set()
            break
    last.add(d)
print(cnt + 1)
