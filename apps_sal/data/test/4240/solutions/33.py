import copy
s = list(input())
t = list(input())
bool = False
for i in range(len(s)):
    temp = copy.copy(s)
    if s == t:
        bool = True
    for j in range(len(s)):
        if j == 0:
            s[0] = temp[len(s) - 1]
        else:
            s[j] = temp[j - 1]
if bool:
    print('Yes')
else:
    print('No')
