T = int(input())
for _ in range(T):
    N, K = list(map(int, input().split()))
    A = [int(a) for a in input().split()]
    m = max(A)
    A = [m - a for a in A]
    if K % 2 == 0:
        m = max(A)
        A = [m - a for a in A]
    print(*A)

