N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))
A.append(float('INF'))
AB = [0] * (N + 1)
j = 0
for i in range(N):
    while A[j] < B[i]:
        j += 1
        if j == N:
            break
    AB[i + 1] = AB[i] + j
ans = 0
B.append(float('INF'))
j = 0
for i in range(N):
    while B[j] < C[i]:
        j += 1
        if j == N:
            break
    ans += AB[j]
print(ans)
