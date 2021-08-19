import sys
Nstr = sys.stdin.readline().strip()
digit_s = 0
for n_i in Nstr:
    digit_s += int(n_i)
if int(Nstr) % digit_s == 0:
    print('Yes')
else:
    print('No')
