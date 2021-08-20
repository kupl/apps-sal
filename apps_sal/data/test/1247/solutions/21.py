l = input()
abc = 'abcdefghijklmnopqrstuvwxyz'
x = sum((l.count(i) % 2 for i in abc))
if x == 0 or x % 2 == 1:
    print('First')
else:
    print('Second')
