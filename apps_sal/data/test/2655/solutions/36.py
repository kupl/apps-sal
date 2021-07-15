import math
N = int(input())
A = list(map(int,input().split()))

list.sort(A, reverse=True)
ans = 0

for i in range(N-1):
#    print(A[math.ceil(i/2)])
    ans += A[math.ceil(i/2)]

print(ans)

