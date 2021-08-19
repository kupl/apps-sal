N = int(input())
s = input()
x = s.count('I')
if x == 0:
    print(s.count('A'))
elif x == 1:
    print(1)
else:
    print(0)
