s = input()
n = len(s)
best = 0
for l in range(n + 1):
    if s[0:l][::-1] != s[0:l]:
        # print(s[:l], s[: l][::-1])
        best = l

print(best)

