N = int(input())
A = list(map(int,input().split()))

ans = [sum(A)//2 - sum([A[i] for i in range(1,N,2)])]

for i in range(N-1):
    ans.append(A[i] - ans[-1])

for x in ans:
    print(2*x, end=" ")
print("")
