S = input()
new_s = ''
for s in S:
    if s == '1':
        new_s += '9'
    else:
        new_s += '1'
print(new_s)
