s = {'H': 0, 'D': 1}
t = 0
a = input().split()
for i in range(2):
    t += s[a[i]]
if t % 2 != 0:
    print('D')
else:
    print('H')
