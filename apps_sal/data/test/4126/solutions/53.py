s = list(input())
n = len(s)
flag = 0
for i in range(n // 2):
    if s[i] != s[n - i - 1]:
        flag = 1
if flag == 0:
    s2 = s[:(n - 1) // 2]
    n2 = len(s2)
    for i in range(n2 // 2):
        if s2[i] != s2[n2 - i - 1]:
            flag = 1
#print(n, n2, s, s2)
if flag == 0:
    if flag == 0:
        s2 = s[(n + 3) // 2 - 1:]
        n2 = len(s2)
    for i in range(n2 // 2):
        if s2[i] != s2[n2 - i - 1]:
            flag = 1
# print(s2)
if flag == 0:
    print("Yes")
else:
    print("No")
