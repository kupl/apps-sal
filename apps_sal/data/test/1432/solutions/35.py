N = int(input())
A = list(map(int, input().split()))

ans = [0 for _ in range(N)]

sign = 1
for a in A:
    ans[0] += sign * a
    sign *= -1


for i in range(1, N):
    ans[i] = 2 * A[0] - ans[i - 1]

    t = A.pop(0)
    A.append(t)

print((*ans))

