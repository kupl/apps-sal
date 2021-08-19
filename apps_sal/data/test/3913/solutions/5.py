n = int(input())
s = input().strip()
m = int(input())
l = []
l1 = []
lmain = []
for i in range(26):
    l.append(0)
    lmain.append(0)
for i in s:
    if i != '*':
        lmain[ord(i) - 97] = 1
for i in range(m):
    s1 = input().strip()
    f = 0
    for j in range(n):
        if s[j] == '*' and lmain[ord(s1[j]) - 97] == 1:
            f = 1
            break
        elif s[j] != '*':
            if s1[j] != s[j]:
                f = 1
                break
    if f == 0:
        l1.append(s1)
length = len(l1)
for i in range(length):
    l2 = []
    s1 = l1[i]
    for j in range(26):
        l2.append(0)
    for j in range(n):
        if s[j] == '*':
            if l2[ord(s1[j]) - 97] != 1:
                l[ord(s1[j]) - 97] += 1
                l2[ord(s1[j]) - 97] = 1
print(l.count(length))
