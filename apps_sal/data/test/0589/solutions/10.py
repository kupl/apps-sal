ans = 1
n = 10
j = 9
d = set()
for i in input():
    if i == '?':
        ans *= min(10, j)
    elif i.isalpha() and i not in d:
        d.add(i)
        ans *= min(n, j)
        n -= 1
    j = 10
print(ans)
