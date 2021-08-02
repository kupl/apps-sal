import math
s = input()
n = len(s)
ans = [0 for _ in range(n)]

count = 0

for i in range(n):
    if s[i] == "R":
        count += 1
    elif s[i] == "L" and count != 0:
        ans[i] += count // 2
        ans[i - 1] += (count + 1) // 2
        count = 0

count = 0
for i in range(n - 1, -1, -1):
    if s[i] == "L":
        count += 1
    elif s[i] == "R" and count != 0:
        ans[i + 1] += (count + 1) // 2
        ans[i] += count // 2
        count = 0

print((' '.join([str(a) for a in ans])))
