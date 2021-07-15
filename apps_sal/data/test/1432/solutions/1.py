N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)

x1 = sum_A - 2 * (sum(A[1:N:2]))

ans = [x1]
for i in range(N):
    if (i == 0):
        continue
    if (i + 1 == N):
        ans.append(2 * A[i] - x1)
        break

    ans.append((2 * A[i - 1]) - ans[i - 1])

print((*ans))

