n = int(input())
s = str(input())
d = True
if len(s) % 2 == 0:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) // 2 + i]:
            d = False
else:
    d = False
if d:
    print('Yes')
else:
    print('No')
