n = int(input())

que = []

for i in range(n):
    t, c = map(int, input().split())
    que += [[t, c]]


numMessages = None
lasReceive = None

maxQ, end = None, None
for i, q in enumerate(que):
    if numMessages == None:
        numMessages = q[1]
        lasReceive = q[0]
        maxQ = numMessages
    
    else:
        numMessages = max(numMessages - (q[0] - lasReceive), 0) + q[1]

        lasReceive = q[0]
    maxQ = max(maxQ, numMessages)
    if i == n - 1:
        print(lasReceive + numMessages, end=' ')
        print(maxQ, end=' ')
        
        
    
