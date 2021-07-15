n = int(input())
s = input()
d = dict()
ans = 0
for i in s:
    if d.get(i) == None:
        d[i] = 1
    else:
        ans = 1
if ans == 1 or n == 1:
    print('Yes')
else:
    print('No')
