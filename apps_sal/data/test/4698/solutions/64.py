N = int(input())
T = list(map(int, input().split()))
ans = sum(T)
M = int(input())
for i in range(M):
    (P, X) = map(int, input().split())
    print(ans - T[P - 1] + X)
