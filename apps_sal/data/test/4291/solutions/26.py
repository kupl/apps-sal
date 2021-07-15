N, Q = map(int, input().split())
S = input()
lr = [list(map(int, input().split())) for _ in range(Q)]

csum = [0]
for i in range(1, N):
    if S[i-1:i+1] == 'AC':
        csum.append(csum[-1]+1)
    else:
        csum.append(csum[-1])
for l, r in lr:
    print(csum[r-1]-csum[l-1])
