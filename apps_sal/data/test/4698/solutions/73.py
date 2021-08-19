N = int(input())
T = input().split()
M = int(input())
for i in range(N):
    T[i] = int(T[i])
S = sum(T)
for i in range(M):
    l = input().split()
    print(S - (T[int(l[0]) - 1] - int(l[1])))
