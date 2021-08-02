import numpy as np
N, K, Q = map(int, input().split())
A = []
for i in range(Q):
    a = int(input())
    A.append(a)
participant = []
for i in range(N):
    participant.append(K)
participant_arr = np.array(participant)
for i in range(Q):
    participant_arr -= 1
    participant_arr[A[i] - 1] += 1
for i in range(N):
    if participant_arr[i] > 0:
        print("Yes")
    else:
        print("No")
