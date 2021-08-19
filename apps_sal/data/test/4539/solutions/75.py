n = input()
s = sum(map(int, list(n)))
if int(n) % s == 0:
    print('Yes')
else:
    print('No')
