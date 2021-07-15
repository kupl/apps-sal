l = int(input())
s = input()
ones = s.count('1')
zeros = l-ones

if s == '0':
    print ('0')
else:
    print ('1' + '0' * zeros)
