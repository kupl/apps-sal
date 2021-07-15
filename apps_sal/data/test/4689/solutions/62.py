K, N = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = 10**18

for i in range(N):
    if i == 0:
        clock_distance = A[N-1] - A[i]
        reverse_distance = K - A[i+1] + A[i]
    elif i == N-1:
        clock_distance = K - A[i] + A[i-1]
        reverse_distance = A[i] - A[0]
    else:
        clock_distance = K - A[i] + A[i+1]
        reverse_distance = K - A[i+1] + A[i]
    ans = min(clock_distance, reverse_distance, ans)

print(ans)




