N = int(input())
A = [int(x) for x in input().split()]
youso = [0] * (10**5 + 1)
for j in range(N):
    youso[A[j]] += 1
ans = sum(A)
Q = int(input())
for i in range(Q):
    B, C = list(map(int, input().split()))
    numofb = youso[B]
    youso[B] = 0
    ans += (C - B) * numofb
    print(ans)
    youso[C] += numofb
