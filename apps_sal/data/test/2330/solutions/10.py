T = int(input())
for t in range(T):
    (n, m) = map(int, input().split())
    A = list(map(int, input().split()))
    tot = sum(A)
    A = [(A[i], i + 1) for i in range(n)]
    A.sort()
    if m < n or n == 2:
        print(-1)
    else:
        cost = 2 * tot
        cost += (m - n) * (A[0][0] + A[1][0])
        print(cost)
        for i in range(n):
            print(i + 1, (i + 1) % n + 1)
        for i in range(m - n):
            print(A[0][1], A[1][1])
