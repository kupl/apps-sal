N = int(input())
T = list(map(int, input().split()))
M = int(input())
for n in range(M):
    P, X = map(int, input().split())
    T_copied = T.copy()
    T_copied[P - 1] = X
    print(sum(T_copied))
