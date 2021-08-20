n = input()
L = len(n)
s = 0
for i in range(L):
    s += int(n[i])
if s % 9 == 0:
    print('Yes')
else:
    print('No')
