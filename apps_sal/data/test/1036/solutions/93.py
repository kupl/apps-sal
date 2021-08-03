from copy import copy
n, k = map(int, input().split())
s = list(input())
if n % 2 != 0:
    s.extend(s)
for i in range(k):
    t = [0] * (len(s) // 2)
    for i in range(len(s) // 2):
        if s[i * 2] == s[i * 2 + 1]:
            t[i] = s[i * 2]
        elif s[i * 2] == "R" and s[i * 2 + 1] == "P" or s[i * 2] == "P" and s[i * 2 + 1] == "S" or s[i * 2] == "S" and s[i * 2 + 1] == "R":
            t[i] = s[i * 2 + 1]
        else:
            t[i] = s[i * 2]
    if len(t) % 2 != 0:
        t.extend(t)
    s = copy(t)
print(t[0])
