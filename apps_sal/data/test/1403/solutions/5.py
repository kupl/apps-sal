def read():
    return int(input())


def readlist():
    return list(map(int, input().split()))


def readmap():
    return map(int, input().split())


N, K = readmap()
A = readlist()

A.sort()

count = 0
same = 1
for i in range(N-1):
    if A[i] == A[i+1]:
        same += 1
    elif A[i+1] <= A[i] + K:
        count += same
        same = 1
    else:
        same = 1

print(N - count)
