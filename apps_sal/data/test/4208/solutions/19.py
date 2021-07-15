n = int(input())
l = input()
r = input()
lc = [[] for i in range(27)]
rc = [[] for i in range(27)]
x = 0
for i in l:
    if i == '?':
        lc[26].append(x)
    else:
        lc[ord(i) - 97].append(x)
    x += 1
x = 0
for i in r:
    if i == '?':
        rc[26].append(x)
    else:
        rc[ord(i) - 97].append(x)
    x += 1
ans = []
ql = []
qr = []
for i in range(26):
    if len(lc[i]) > len(rc[i]):
        for t in range(len(lc[i]) - len(rc[i])):
            ql.append(lc[i].pop())
    else:
        for t in range(len(rc[i]) - len(lc[i])):
            qr.append(rc[i].pop())
    for j in range(len(lc[i])):
        ans.append([lc[i].pop(), rc[i].pop()])
for i in range(min(len(ql), len(rc[26]))):
    ans.append([ql.pop(), rc[26].pop()])
for i in range(min(len(qr), len(lc[26]))):
    ans.append([lc[26].pop(), qr.pop()])
for i in range(min(len(lc[26]), len(rc[26]))):
    ans.append([lc[26].pop(), rc[26].pop()])
print(len(ans))
for i in ans:
    print(i[0] + 1, i[1] + 1)

