n = int(input())
s = []
for i in range(n):
    s.append(input())
c = {}
for i in s:
    if any((i in d for d in c)):
        c[i] = c[i] + 1
    else:
        c[i] = 1
max = 1
for key in c:
    if c[key] > max:
        max = c[key]
print(max)
