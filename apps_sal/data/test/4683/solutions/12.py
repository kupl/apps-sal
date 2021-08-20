N = int(input())
A = list(map(int, input().split()))
s = 0
s2 = sum(A)
for i in range(N - 1):
    s2 -= A[i]
    s += A[i] * s2
answer = s % (10 ** 9 + 7)
print(answer)
