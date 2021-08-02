N = list(map(int, list(str(int(input())))))
if sum(N) % 9 == 0:
    print('Yes')
else:
    print('No')
