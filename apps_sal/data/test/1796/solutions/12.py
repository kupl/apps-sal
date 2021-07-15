import sys

n = int(input())
i = 0
res = 0
while (i < n):
    s = input()
    if (s[1] == '+'):
        res = res + 1
    else:
        res = res - 1
    i = i + 1
print(res)
    


