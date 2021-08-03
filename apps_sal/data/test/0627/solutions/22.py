n = int(input())
s = str(input())
flag = 0
k = ''
for i in range(1, n):
    if(s[i - 1] > s[i]):
        k = s[:i - 1] + s[i:]
        flag = 1
        break
if(flag == 0):
    k = s[:-1]
print(k)
