N = int(input())
W = [input() for _ in range(N)]

if len(set(W)) != N:
    print('No')
    return

for i in range(1, N):
    if W[i][0] != W[i-1][-1]:
        print('No')
        return
print('Yes')

