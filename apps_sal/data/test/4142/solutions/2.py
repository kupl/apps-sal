import re
string = input()
pattern = re.compile('^([^L][^R])*[^L]?$')
if pattern.match(string):
    print('Yes')
else:
    print('No')
