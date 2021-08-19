x = input().split()
d = int(x[0])
t = int(x[1])
s = int(x[2])
if d / t <= s:
    print('Yes')
else:
    print('No')
