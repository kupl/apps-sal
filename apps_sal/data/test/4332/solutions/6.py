n = input()
m = list(n)
m = list(map(int,m))
m = sum(m)
if int(n) % m == 0:
    print('Yes')
else:
    print('No')
