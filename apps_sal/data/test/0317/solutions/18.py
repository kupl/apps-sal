n = int(input())
str = input().lower()
x = [0] * 50
for i in range(n) :
    x[ord(str[i]) - ord('a')] = 1
cou = 0
for i in range(26) :
    cou += x[i]
if cou >= 26:
    print('YES')
else :
    print('NO')
