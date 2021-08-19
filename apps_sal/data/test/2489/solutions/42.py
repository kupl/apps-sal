N = int(input())
A = list(map(int, input().split()))
A.sort()
INF = 10 ** 6 + 1
lis = [1] * INF
exist = [0] * INF
for i in range(N):
    a = A[i]
    if lis[a] and exist[a] < 1:
        q = 2
        while a * q < INF:
            lis[a * q] = 0
            q += 1
    exist[a] += 1
cnt = 0
for a in A:
    if lis[a] and exist[a] == 1:
        cnt += 1
print(cnt)
