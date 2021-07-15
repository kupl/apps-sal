import re

string = input()
pattern = re.compile(r'^([^L][^R])*[^L]?$')
if pattern.match(string):
    print('Yes')
else:
    print('No')
