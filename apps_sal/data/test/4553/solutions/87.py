import re

A, B = map(int, input().split())
S = input()

former = S[0:A]
later = S[(A + 1):(A + B + 3)]

r_f = re.compile('\d{' + str(A) + '}')
r_l = re.compile('\d{' + str(B) + '}')

if r_f.findall(former) and r_l.findall(later) and S[A] == '-':
    print('Yes')
else:
    print('No')
