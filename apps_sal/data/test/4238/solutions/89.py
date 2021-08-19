N = input()
n = list(map(int, N))
if sum(n) % 9 == 0:
    print('Yes')
else:
    print('No')
