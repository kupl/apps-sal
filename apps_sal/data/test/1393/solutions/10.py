s = input()
t = input()
c = -ord('A') + ord('a')
ura = 0
opa = 0
s2 = set()
ind = set()
s1 = dict()
for i in range(len(s)):
    if ord(s[i]) not in s2:
        s2.add(ord(s[i]))
        s1[ord(s[i])] = 1
    else:
        s1[ord(s[i])] += 1
for i in range(len(t)):
    if ord(t[i]) in s2 and s1[ord(t[i])] >= 1:
        s1[ord(t[i])] -= 1
        ura += 1
        ind.add(i)
for i in range(len(t)):
    if i not in ind:
        if ord('z') >= ord(t[i]) >= ord('a'):
            if ord(t[i]) - c in s2 and s1[ord(t[i]) - c] >= 1:
                opa += 1
                s1[ord(t[i]) - c] -= 1
                ind.add(i)
        elif ord(t[i]) + c in s2 and s1[ord(t[i]) + c] >= 1:
            opa += 1
            s1[ord(t[i]) + c] -= 1
            ind.add(i)
print(ura, opa)
