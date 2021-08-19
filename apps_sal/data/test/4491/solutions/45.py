N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
sum1 = [0]
sum2 = [0]
for i in range(N):
    sum1.append(sum1[-1] + A[0][i])
    sum2.append(sum2[-1] + A[1][i])
print(max((sum1[i] + sum2[N] - sum2[i - 1] for i in range(1, N + 1))))
