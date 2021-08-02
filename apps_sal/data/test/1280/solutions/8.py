s = input()
a = input()
k = int(input())
d = sorted(s[i:] for i in range(len(s)))

c = ''
r = 0

for j in d:
    pos = 0
    s = 0
    for i in range(len(j)):
        if i >= len(c) or j[i] != c[i]:
            s = 1
        if a[ord(j[i]) - ord('a')] == '0':
            pos += 1
        if pos > k:
            break
        if s:
            r += 1
    c = j
print(r)
