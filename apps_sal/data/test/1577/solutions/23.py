n = int(input())
s = input()
c1 = 0
c2 = 0
for i in range(n):
    if s[i] == 'A':
        c1 += 1
    else:
        c2 += 1
if c1 == c2:
    print('Friendship')
elif c1 > c2:
    print('Anton')
else:
    print('Danik')
