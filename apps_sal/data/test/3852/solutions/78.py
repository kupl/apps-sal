N = int(input())
A = list(map(int, input().split()))

MIN, MAX = 10**7, -10**7
ans = []
for i in range(N):
    if MIN > A[i]:
        MIN = A[i]
        min_i = i
    if MAX < A[i]:
        MAX = A[i]
        max_i = i

if abs(MIN) <= abs(MAX):
    for i in range(N):
        if A[i] < 0:
            A[i] += MAX
            ans.append([max_i + 1, i + 1])
    # print(A)

    for i in range(N - 1):
        if A[i] > A[i + 1]:
            A[i + 1] += A[i]
            ans.append([i + 1, i + 2])

else:
    for i in range(N):
        if A[i] > 0:
            A[i] += MIN
            ans.append([min_i + 1, i + 1])
    # print(A)

    for i in range(N - 1, 0, -1):
        if A[i] < A[i - 1]:
            A[i - 1] += A[i]
            ans.append([i + 1, i])
print((len(ans)))
for a in ans:
    print((*a))
