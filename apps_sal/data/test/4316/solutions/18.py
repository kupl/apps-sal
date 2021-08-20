s = input()
lst = []
for i in range(4):
    lst.append(s[i])
ans = 0
for i in range(4):
    if lst.count(lst[i]) != 2:
        ans = 1
if ans == 0:
    print('Yes')
else:
    print('No')
