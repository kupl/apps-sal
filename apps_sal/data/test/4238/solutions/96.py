from sys import stdin
N = list(stdin.readline().rstrip())
d_sum = 0
for n in N:
    d_sum += int(n)
if d_sum % 9 == 0:
    print('Yes')
else:
    print('No')
