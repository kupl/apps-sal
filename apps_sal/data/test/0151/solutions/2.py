s = input()
n = len(s)
sogl = ['a', 'e', 'i', 'o', 'u']
i = 0
ans = []
while i < n - 2:
    if not(s[i] in sogl) and not(s[i + 1] in sogl) and not(s[i + 2] in sogl) and not(s[i] == s[i + 1] == s[i + 2]):
        ans.append(i + 2)
        i += 1
    i += 1
j = 0
for i in ans:
    print(s[j:i], end=" ")
    j = i
print(s[j:])
