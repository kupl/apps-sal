s = list(map(str, input()))

if len(s) == len(set(s)):
    print('yes')
else:
    print('no')
