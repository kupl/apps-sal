s = list(input())
r = 0
for ii in range(len(s) - 1):
    if s[ii + 1] != s[ii]:
        r += 1
print(r)
