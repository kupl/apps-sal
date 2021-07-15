n = input()
ans = 0
for i in n:
    ans += int(i)
check = str(int(n) / ans)

if check[-1] == '0':
    print('Yes')
else:
    print('No')
