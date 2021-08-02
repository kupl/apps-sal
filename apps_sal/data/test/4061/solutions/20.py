s = input()
t = input()
indl = [-1 for i in range(len(t))]
j = 0
for i in range(len(s)):
    if s[i] == t[j]:
        indl[j] = i
        j += 1
        if j == len(t):
            break
indr = [-1 for i in range(len(t))]
j = len(t) - 1
for i1 in range(len(s)):
    i = len(s) - 1 - i1
    if s[i] == t[j]:
        indr[j] = i
        j -= 1
        if j == -1:
            break
l = indr[0]
for i in range(len(t) - 1):
    l = max(l, indr[i + 1] - indl[i] - 1)
l = max(l, len(s) - 1 - indl[len(t) - 1])
print(l)
