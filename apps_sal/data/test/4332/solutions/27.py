n = input()
l = [int(i) for i in n]
if int(n) % sum(l) == 0:
    print('Yes')
else:
    print('No')
