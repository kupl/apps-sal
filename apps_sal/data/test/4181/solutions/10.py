n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans = 0
B.append(0)

for i in reversed(list(range(n))):
    if B[i] <= A[i] + A[i + 1]:
        ans += B[i]
        if B[i] < A[i + 1]:
            A[i] = A[i]
        else:
            A[i] = A[i] - (B[i] - A[i + 1])
    else:
        ans += A[i] + A[i + 1]
        A[i] = 0
print(ans)
