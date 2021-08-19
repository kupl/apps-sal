s = input()
n = len(s)
best = 0
for l in range(n + 1):
    if s[0:l][::-1] != s[0:l]:
        best = l
print(best)
