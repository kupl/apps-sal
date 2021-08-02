import re
A, B = input().split()
S = input()

my_regex = r"\d{" + A + r"}-\d{" + B + r"}"

if re.fullmatch(my_regex, S) == None:
    print('No')

else:
    print('Yes')
