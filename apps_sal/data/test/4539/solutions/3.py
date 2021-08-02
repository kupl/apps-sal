n = input()
m = list(n)
m = list(map(int, m))
if int(n) % sum(m) == 0:
    print('Yes')
else:
    print('No')
