(N, K, Q) = map(int, input().split())
attendee = [K - Q] * N
A = [0] * Q
for i in range(Q):
    A[i] = int(input())
for i in range(Q):
    attendee[A[i] - 1] += 1
'\nfor i in range(Q):\n    attendee = list(map(lambda x: x-1, attendee))\n    attendee[A[i]-1]+=1 #添字に注意(1つずれる)\n'
for i in range(N):
    if attendee[i] <= 0:
        print('No')
    else:
        print('Yes')
