a = input()
b = a[2:len(a) - 1]
if a[0] == 'A' and b.count('C') == 1 and (len(a) - sum((1 for i in a if i.islower())) == 2):
    print('AC')
else:
    print('WA')
