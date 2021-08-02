N = int(input())
A = list(map(int, input().split()))

DP_odd = [0, 0, A[0]]
DP_even = [0, max(A[0], A[1])]

if N >= 3:
    DP_odd = [DP_even[0], max(DP_odd[1] + A[2], DP_even[1]), DP_odd[2] + A[2]]

for i in range(3, N):
    if (i + 1) % 2 == 1:
        DP_odd = [max(DP_odd[0] + A[i], DP_even[0]), max(DP_odd[1] + A[i], DP_even[1]), DP_odd[2] + A[i]]
    else:
        DP_even = [max(DP_even[0] + A[i], DP_odd[1]), max(DP_even[1] + A[i], DP_odd[2])]

if N % 2 == 1:
    ans = DP_odd[1]
else:
    ans = DP_even[1]

print(ans)
