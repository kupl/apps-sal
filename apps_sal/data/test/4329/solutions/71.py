s = list(input())
t = list(input())
flag = 0
if (len(s) + 1) == len(t):
    for i in range(len(s)):
        if s[i] != t[i]:
            flag = 1
    if flag == 1:
        print('No')
    else:
        print('Yes')
else:
    print('No')
