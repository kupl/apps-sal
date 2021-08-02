T = int(input())
for _ in range(T):
    N, S = map(int, input().split())
    A = [int(a) for a in input().split()]
    if S >= sum(A):
        print(0)
    else:
        ma = 0
        mai = -1
        s = 0
        for i in range(N):
            s += A[i]
            if A[i] > ma:
                ma = A[i]
                mai = i + 1
            if s > S:
                print(mai)
                break
