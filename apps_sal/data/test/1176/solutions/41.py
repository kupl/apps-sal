N = int(input())
A = list(map(int, input().split()))

plus = 0
zero = 0
minus = 0

for i in range(N):
    if A[i] > 0:
        plus += 1
    elif A[i] < 0:
        minus += 1
    else:
        zero += 1
ans = 0
m = 10**9 + 10
for i in range(N):
    ans += abs(A[i])
    m = min(m, abs(A[i]))


if minus % 2 == 0 or zero > 0:
    pass
else:

    ans = ans - 2 * m

print(ans)
