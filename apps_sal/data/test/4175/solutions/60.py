N = int(input())
W = []
for i in range(N):
    W.append(input())

False_cnt = 0
for i in range(N):
    if W.count(W[i]) >= 2:
        False_cnt += 1

for i in range(N-1):
    x = W[i]
    y = W[i + 1]
    if not x[-1] == y[0]:
        False_cnt += 1

if False_cnt == 0:
    print('Yes')
else:
    print('No')
