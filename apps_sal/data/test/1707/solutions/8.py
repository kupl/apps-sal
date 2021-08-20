N = int(input())
A = sorted([abs(int(a)) for a in input().split()])
i = 0
j = 1
ans = 0
while j < N:
    while j < N - 1 and A[j + 1] <= A[i] * 2:
        j += 1
    if A[j] <= A[i] * 2:
        ans += j - i
    i += 1
    if j == i:
        j += 1
print(ans)
