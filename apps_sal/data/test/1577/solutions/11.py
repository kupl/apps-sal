n = int(input())
s = input()
a = d = 0
for i in s:
    if i == 'A':
        a += 1
    else:
        d += 1
if a > d:
    print('Anton')
elif a < d:
    print('Danik')
else:
    print('Friendship')
