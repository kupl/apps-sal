import re
A, B = map(int, input().split())
S = input()
pattern = re.compile('[0-9]'*A + '-' +'[0-9]'*B)
print('Yes' if pattern.fullmatch(S) != None else 'No')
