n = int(input())
s = str(n)
ds = 0
for c in s:
    ds += int(c)
if n % ds == 0:
    print('Yes')
else:
    print('No')
