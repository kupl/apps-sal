N = int(input())
A = list(map(int,input().split()))

ans = [-1] * N
for i,a in enumerate(A):
    ans[a-1] = i+1
print((*ans))

