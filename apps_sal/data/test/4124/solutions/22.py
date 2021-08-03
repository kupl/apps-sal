s = input()
s1 = input()
s = s[::-1]
s1 = s1[::-1]
ans = -1
for i in range(min(len(s), len(s1))):
    if s[i] != s1[i]:
        ans = i
        break
if ans == -1:
    ans = min(len(s), len(s1))
print(len(s) + len(s1) - ans * 2)
