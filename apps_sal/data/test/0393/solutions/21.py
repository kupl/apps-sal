n = int(input())
s = input()
i = 0
res = True
count = 0
while i < n:
    if s[i] == '1':
        if count > 2 or (i != 0 and count == 0):
            res = False
            break
        count = 0
    else:
        count += 1
    i += 1
if n == 1 and s[0] == '0' or (n > 1 and s[0] == '0' and (s[1] == '0')):
    res = False
if count >= 2:
    res = False
if res:
    print('Yes')
else:
    print('No')
