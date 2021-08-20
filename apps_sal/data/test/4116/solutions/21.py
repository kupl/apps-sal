N = int(input())
L = [x * y for x in range(1, 10) for y in range(1, 10)]
if L.count(N) != 0:
    print('Yes')
else:
    print('No')
