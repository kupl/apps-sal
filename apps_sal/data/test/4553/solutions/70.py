import re
import sys
A, B = map(int, input().split())
S = input()

if S[A] != '-':
    print('No')
    return

S = S.replace('-', '')

if len(S) == 0:
    print('No')
    return

count = 0
for i in range(len(S)):
    if re.match(r'[0-9]', S[i]):
        count += 1

if count == A+B:
    print('Yes')
else:
    print('No')
