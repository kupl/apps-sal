N,K,Q = map(int, input().split())

score = [K-Q]*N

for i in range(Q):
    temp = int(input())
    score[temp-1] += 1

for j in score:
    if j > 0:
        print('Yes')
    else:
        print('No')
