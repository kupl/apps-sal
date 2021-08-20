s = input()
t = input()
lefts = [0 for i in range(len(t))]
rights = [0 for i in range(len(t))]
i = 0
j = 0
while i < len(s) and j < len(t):
    if s[i] == t[j]:
        lefts[j] = i
        j += 1
    i += 1
i = len(s) - 1
j = len(t) - 1
while i >= 0 and j >= 0:
    if s[i] == t[j]:
        rights[j] = i
        j -= 1
    i -= 1
ans = max(len(s) - lefts[-1] - 1, rights[0])
for i in range(len(t) - 1):
    ans = max(ans, rights[i + 1] - lefts[i] - 1)
print(ans)
