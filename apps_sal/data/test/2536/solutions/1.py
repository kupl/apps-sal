(N, M) = map(int, input().split())
arr = []
for i in range(0, N):
    k = list(map(int, input().split()))
    arr.append(k)
E1 = 0
E2 = 0
L = int(input())
f1 = 0
f2 = 0
for j in range(0, L):
    (a, b) = map(int, input().split())
    if a > N or b > M:
        E1 = -1
        f1 = 1
    elif f1 == 0:
        E1 += arr[a - 1][b - 1]
    if b > N or a > M:
        E2 = -1
        f2 = 1
    elif f2 == 0:
        E2 += arr[b - 1][a - 1]
print(max(E1, E2))
