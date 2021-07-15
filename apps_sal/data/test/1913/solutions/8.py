import sys

n = int(input())
l = input().split()
zero = 0
a = 0
for x in l:
    onec = x.count('1')
    zeroc = x.count('0')
    if x == '0':
        print(0)
        return
    elif onec == 1 and zeroc == len(x) - 1:
        zero += x.count('0')
    else:
        a = x

if a:
    ans = a + ('0' * zero)
else:
    ans = '1' + ('0' * zero)
print(ans)

