n = input()
sn = sum([int(n[i]) for i in range(len(n))])
n = int(n)
if n % sn == 0:
    print('Yes')
else:
    print('No')
