x = int(input())
s = input()
if s.count('I') > 1:
    print(0)
elif s.count('I') == 0:
    print(s.count('A'))
else:
    print(1)
