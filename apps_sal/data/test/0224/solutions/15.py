s = input()
d = ['A', 'E', 'I', 'O', 'U', 'Y']
p = 0
m = 0
for i in range(len(s)):
    if s[i] in d:
        if i + 1 - p > m:
            m = i + 1 - p
        p = i + 1
if len(s) + 1 - p > m:
    m = len(s)  + 1 - p
print(m)
