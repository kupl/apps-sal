s = input()
S = ''
for i in s:
    if i in 'ACGT':
        S += '1'
    else:
        S += '0'
print(max(list(map(len, S.split('0')))))
