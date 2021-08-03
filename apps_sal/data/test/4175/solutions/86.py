n = int(input())
s = []
for i in range(n):
    s.append(input())
total = True
for i in range(n - 1):
    if s[i][-1] != s[i + 1][0]:
        total = False
        break
    for j in range(len(s)):
        if i != j:
            if s[i] == s[j]:
                total = False
                break
    if total == False:
        break
if total == False:
    print("No")
else:
    print("Yes")
