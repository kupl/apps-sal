n = int(input())
s = input()
a = 0
d = 0
for i in s:
    a += i == 'A'
    d += i == 'D'
if a > d:
    print('Anton')
elif a == d:
    print('Friendship')
else:
    print('Danik')
