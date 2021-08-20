import re
(A, B) = input().split()
S = input()
my_regex = '\\d{' + A + '}-\\d{' + B + '}'
if re.fullmatch(my_regex, S) == None:
    print('No')
else:
    print('Yes')
