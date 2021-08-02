N = int(input())
A = [int(input()) for _ in range(N)]
sort_A = sorted(A, reverse=True)
ans = []

for i in range(N):
    if sort_A[0] == A[i]:
        ans.append(sort_A[1])
    else:
        ans.append(sort_A[0])

for a in ans:
    print(a)
