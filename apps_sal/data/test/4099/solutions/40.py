N,K,M = map(int,input().split())
A = list(map(int,input().split()))

all = sum(A)
goal = M * N

last = goal - all

if last > K:
    print(-1)
elif last < 0:
    print(0)
else:
    print(last)
