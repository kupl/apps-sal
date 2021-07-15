s = input()
t = input()

l_s = [[] for _ in range(26)]

for i, x in enumerate(s):
    l_s[ord(x) - 97].append(i)

l_t = [[] for _ in range(26)]
for i, x in enumerate(t):
    l_t[ord(x) - 97].append(i)

for l in l_s:
    if len(l) > 0:
        if l_t[ord(t[l[0]]) - 97] != l:
            print('No')
            return

print('Yes')
