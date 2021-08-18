N, K, Q = map(int, input().split())

attendee = [(K - Q)] * N
A = [0] * Q

for i in range(Q):
    A[i] = int(input())

for i in range(Q):
    attendee[A[i] - 1] += 1

"""
for i in range(Q):
    attendee = list(map(lambda x: x-1, attendee))
    attendee[A[i]-1]+=1 
"""

for i in range(N):
    if attendee[i] <= 0:
        print("No")
    else:
        print("Yes")
