s = input()
i = (len(s) - 1) // 2
j = len(s) // 2
k = s[i]
while i >= 0:
    if s[i] != k or s[j] != k:
        break
    i -= 1
    j += 1
if i < 0:
    print(len(s))
else:
    print(j)
