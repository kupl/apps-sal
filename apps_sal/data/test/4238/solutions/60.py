s = input()
n = len(s)
all = int(0)
for i in range(n):
    all += int(s[i])
if all % 9 == 0:
    print('Yes')
else:
    print('No')
