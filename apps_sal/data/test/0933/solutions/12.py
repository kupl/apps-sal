s = list(input())
x = []
for c in s:
    i = len(x)
    if i >= 2 and x[i - 2] == x[i - 1] and (x[i - 1] == c):
        continue
    if i >= 3 and x[i - 3] == x[i - 2] and (x[i - 1] == c):
        continue
    x.append(c)
print(''.join(x))
