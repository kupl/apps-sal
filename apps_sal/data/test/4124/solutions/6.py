s = input()
t = input()
k = 0
for i in range(min(len(s), len(t))):
    if s[len(s) - 1 - i] == t[len(t) - 1 - i]:
        k = k + 1
    else:
        break
print(len(s) - 2 * k + len(t))
