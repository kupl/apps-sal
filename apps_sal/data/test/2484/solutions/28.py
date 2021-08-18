N = int(input())
A = list(int(a) for a in input().split())

ans = 0
x_sum = 0
a_sum = 0
r = 0
for l in range(N):
    while r < N and x_sum ^ A[r] == a_sum + A[r]:
        x_sum ^= A[r]
        a_sum += A[r]
        r += 1
    ans += r - l
    x_sum ^= A[l]
    a_sum -= A[l]

print(ans)
