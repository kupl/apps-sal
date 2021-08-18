def inputlist(): return [int(j) for j in input().split()]


N = int(input())
A = inputlist()
sum_A = sum(A)
left = 0
ans = 10**9 + 7
for i in range(N):
    left += A[i]
    sum_A -= A[i]
    ans = min(abs(sum_A - left), ans)
print(ans)
