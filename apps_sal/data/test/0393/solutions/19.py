input()
s = input()
if s == '0':
    print('No')
elif s.startswith('00') or s.endswith('00'):
    print('No')
else:
    print('No' if s.find('11') != -1 or s.find('000') != -1 else 'Yes')
