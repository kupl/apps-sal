N = int(input())
NN = sum(list(map(int, str(N))))
if N % NN == 0:
    print('Yes')
else:
    print('No')
