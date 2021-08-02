n = int(input())
s = []
res = "Yes"
for i in range(n):
    s.append(input())
    for j in range(i):
        if s[i] == s[j]:
            res = "No"
    if i != 0:
        if s[i][0] != s[i - 1][len(s[i - 1]) - 1]:
            res = "No"
print(res)
