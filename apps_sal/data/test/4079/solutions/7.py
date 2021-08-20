alf = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
for i in range(n):
    string = ''.join(sorted(list(input())))
    if string in alf:
        print('Yes')
    else:
        print('No')
