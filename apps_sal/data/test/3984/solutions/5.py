s = input()
min_val = 9999
for c in s:
    if min_val < ord(c):
        print('Ann')
    else:
        print('Mike')
    min_val = min(min_val, ord(c))
