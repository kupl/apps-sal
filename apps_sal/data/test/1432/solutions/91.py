

N = int(input())
A = list(map(int, input().split()))


s = sum(A)
x = s - sum(A[1::2]) * 2
ans = [x]
for i in range(N - 1):
    x = 2 * A[i] - x
    ans += [x]
print((*ans))
