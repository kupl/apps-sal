N = int(input())
A = list(map(int, input().split()))

rev = [i for i in range(N)]
for i in range(N):
    rev[A[i]-1] = i+1
print((*rev))

