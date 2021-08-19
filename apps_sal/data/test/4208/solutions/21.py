n = int(input())
l = list(input())
r = list(input())
la = [[] for i in range(26)]
ra = [[] for i in range(26)]
ir = []
il = []
for i in range(n):
    if l[i] != '?':
        la[ord(l[i]) - ord('a')].append(i)
    else:
        il.append(i)
for i in range(n):
    if r[i] != '?':
        ra[ord(r[i]) - ord('a')].append(i)
    else:
        ir.append(i)
ans = []
for i in range(26):
    while len(la[i]) > 0 and len(ra[i]) > 0:
        (x, y) = (la[i].pop(), ra[i].pop())
        ans.append([x + 1, y + 1])
for i in range(26):
    while len(ir) > 0 and len(la[i]) > 0:
        (x, y) = (la[i].pop(), ir.pop())
        ans.append([x + 1, y + 1])
for i in range(26):
    while len(il) > 0 and len(ra[i]) > 0:
        (x, y) = (il.pop(), ra[i].pop())
        ans.append([x + 1, y + 1])
while len(il) > 0 and len(ir) > 0:
    (x, y) = (il.pop(), ir.pop())
    ans.append([x + 1, y + 1])
print(len(ans))
for i in ans:
    print(*i)
