# Author: Tanya Cheremkhina
n = int(input())
s = list(input())
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        s[i] = ''
        break
else:
    s[-1] = ''
print(''.join(s))
