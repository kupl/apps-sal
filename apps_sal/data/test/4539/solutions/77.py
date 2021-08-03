n = input()
f = 0
for i in range(len(n)):
    f += int(n[i])
if int(n) % f == 0:
    print('Yes')
else:
    print('No')
