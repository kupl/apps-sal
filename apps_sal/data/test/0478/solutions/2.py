import sys

# inf = open('input.txt', 'r')
# reader = (line.rstrip() for line in inf)
reader = (line.rstrip() for line in sys.stdin)
input = reader.__next__

n = int(input())
s = [ord(c) for c in input()]
ans = 0
code = 122
while code >= 97:
    toDel = []
    k = len(s)
    for i, c in enumerate(s):
        if c != code:
            continue
        if i > 0 and s[i - 1] + 1 == code:
            toDel.append(i - len(toDel))
        elif i < k - 1 and s[i + 1] + 1 == code:
            toDel.append(i - len(toDel))
    if toDel:
        for i in toDel:
            del s[i]
            ans += 1
    else:
        code -= 1
print(ans)

# inf.close()

