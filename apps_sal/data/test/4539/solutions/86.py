n = input()
a = 0
for i in range(len(n)):
    a += int(n[i])

x = int(n)
if x % a == 0:
    print('Yes')
else:
    print('No')
