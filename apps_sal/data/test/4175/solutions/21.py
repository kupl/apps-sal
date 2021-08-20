N = int(input())
W = list((input() for i in range(N)))
for i in range(N - 1):
    if W.count(W[i]) == 2:
        print('No')
        break
    if W[i][-1] != W[i + 1][0]:
        print('No')
        break
else:
    print('Yes')
