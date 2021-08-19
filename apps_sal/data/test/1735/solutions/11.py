s = input()
x = []
ans = 0
for i in s:
    x.append(i)
    if len(x) >= 2 and x[-1] == x[-2]:
        ans += 1
        x.pop()
        x.pop()
if ans % 2 == 0:
    print('No')
else:
    print('Yes')
