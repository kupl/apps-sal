import sys
input = sys.stdin.readline

Q = int(input())
Query = []
for _ in range(Q):
    N = int(input())
    A = list(map(int, input().split()))
    Query.append((N, A))

for N, A in Query:
    A.sort()
    l = 0
    r = N - 1
    ans = []
    for i in range(N):
        if i % 2 == 0:
            ans.append(str(A[l]))
            l += 1
        else:
            ans.append(str(A[r]))
            r -= 1
    print(" ".join(ans[::-1]))
