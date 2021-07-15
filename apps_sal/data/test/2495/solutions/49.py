N = int(input())
A = list(map(int, input().split()))

if A[0] > 0:
    A_sum = A[0]
    ans1 = 0
else:
    A_sum = 1
    ans1 = 1-A[0]
for i in range(1, N):
    if A_sum < 0:
        A_sum += A[i]
        if A_sum <= 0:
            ans1 += 1 - (A_sum)
            A_sum = 1
    elif A_sum > 0:
        A_sum += A[i]
        if A_sum >= 0:
            ans1 += (A_sum) - (-1)
            A_sum = -1


if A[0] < 0:
    A_sum = A[0]
    ans2 = 0
else:
    A_sum = -1
    ans2 = A[0]-(-1)
for i in range(1, N):
    if A_sum < 0:
        A_sum += A[i]
        if A_sum <= 0:
            ans2 += 1 - (A_sum)
            A_sum = 1
    elif A_sum > 0:
        A_sum += A[i]
        if A_sum >= 0:
            ans2 += (A_sum) - (-1)
            A_sum = -1



print((min(ans1, ans2)))

