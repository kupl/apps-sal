import collections
N = int(input())
lsa = list(map(str, input().split()))
lsb = collections.deque()
if N % 2 == 0:
    for i in range(N):
        if i % 2 == 0:
            lsb.append(lsa[i])
        else:
            lsb.appendleft(lsa[i])
if N % 2 == 1:
    for i in range(N):
        if i % 2 == 1:
            lsb.append(lsa[i])
        else:
            lsb.appendleft(lsa[i])

print(' '.join(lsb))
