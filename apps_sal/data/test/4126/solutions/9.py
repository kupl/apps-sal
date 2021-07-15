import math
s = list(input())
n = len(s)
s1 = s[ : (n-1) // 2]
s2 = s[(n+3) // 2 - 1 : n]
flag = 1

for i in range(len(s) // 2):
    if s[i] != s[- i - 1]:
        flag = 0

for i in range(len(s1) // 2):
    if s1[i] != s1[- i - 1]:
        flag = 0

for i in range(len(s2) // 2):
    if s2[i] != s2[- i - 1]:
        flag = 0

print(('Yes' if flag == 1  else 'No'))

