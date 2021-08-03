s = input()
a = s[0]
b = s[len(s) - 1]
n = len(s) % 2
if n == 1 and a == b:
    print('Second')
elif n == 1 and a != b:
    print('First')
elif n == 0 and a == b:
    print('First')
else:
    print('Second')
