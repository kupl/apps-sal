# import collections

s = input()

a = ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']

for i in range(len(a)):
    if s.find(a[i]) != -1:
        print('Yes')
        return

print('No')
