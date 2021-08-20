n = input()
ans = 0
for i in n:
    ans += int(i)
if int(n) % ans == 0:
    print('Yes')
else:
    print('No')
