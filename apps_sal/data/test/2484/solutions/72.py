N = int(input())
A = list(int(a) for a in input().split())

ans = 0
x_sum = 0
a_sum = 0
r = -1
for l in range(N):
    while x_sum == a_sum and r < N-1:
        r += 1
        x_sum ^= A[r]
        a_sum += A[r]
    if x_sum != a_sum:
        x_sum ^= A[r]
        a_sum -= A[r]
        r -= 1
    ans += r-l+1
    #print(l, r, x_sum, a_sum, ans)
    x_sum ^= A[l]
    a_sum -= A[l]

print(ans)
