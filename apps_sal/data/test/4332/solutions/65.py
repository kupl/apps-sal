li = list(map(int, input()))
N = 0
for i in range(len(li)):
    N = N + li[len(li) - 1 - i] * 10**i
S = sum(li)
if N % S == 0:
    print('Yes')
else:
    print('No')
