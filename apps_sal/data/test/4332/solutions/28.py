n = input()
if int(n) % sum(list(map(int, list(n)))) == 0:
    print('Yes')
else:
    print('No')
