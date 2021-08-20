lst = input().split()
A = int(lst[0])
B = int(lst[1])
s = input()
if len(s) == A + B + 1 and s.count('-') == 1 and (s[A] == '-'):
    print('Yes')
else:
    print('No')
