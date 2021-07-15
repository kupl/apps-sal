n = int(input())
s1 = input()
s2 = input()
a1 = [0 for i in range(26)]
b1 = [[] for i in range(26)]
a2 = [0 for i in range(26)]
b2 = [[] for i in range(26)]
v1 = []
v2 = []
cntv1 = 0
for i in range(n):
    if s1[i] == '?':
        cntv1 += 1
        v1.append(i)
    else:
        a1[ord(s1[i]) - 97] += 1
        b1[ord(s1[i]) - 97].append(i)
cntv2 = 0
for i in range(n):
    if s2[i] == '?':
        cntv2 += 1
        v2.append(i)
    else:
        a2[ord(s2[i]) - 97] += 1
        b2[ord(s2[i]) - 97].append(i)
cnt = 0
c = []

for i in range(26):
    while a1[i] > 0 and a2[i] > 0:
        cnt += 1
        a1[i] -= 1
        a2[i] -= 1
        c.append([b1[i].pop() + 1, b2[i].pop() + 1])
for i in range(26):
    while a1[i] > 0 and cntv2 > 0:
        cntv2 -= 1
        a1[i] -= 1
        cnt += 1
        c.append([b1[i].pop() + 1, v2.pop() + 1])
for i in range(26):
    while a2[i] > 0 and cntv1 > 0:
        cntv1 -= 1
        a2[i] -= 1
        cnt += 1
        c.append([v1.pop() + 1, b2[i].pop() + 1])
if cntv2 != 0 and cntv1 != 0:
    while cntv2 > 0 and cntv1 > 0:
        cnt += 1
        cntv1 -= 1
        cntv2 -= 1
        c.append([v1.pop() + 1, v2.pop() + 1])
print(cnt)
for i in range(len(c)):
    print(*c[i])

