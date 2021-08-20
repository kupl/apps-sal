s = input()
n = len(s)
first = [0] * n
last = [0] * n
p = 0
c = 0
for i in range(n):
    if s[i] == 'v':
        p += 1
    else:
        if p:
            c += p - 1
        p = 0
    if s[i] == 'o':
        first[i] = c
p = 0
c = 0
for i in range(n - 1, -1, -1):
    if s[i] == 'v':
        p += 1
    else:
        if p:
            c += p - 1
        p = 0
    if s[i] == 'o':
        last[i] = c
result = 0
for i in range(n):
    if s[i] == 'o':
        result += first[i] * last[i]
print(result)
