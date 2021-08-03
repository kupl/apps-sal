N = int(input())
A = list(map(int, input().split()))
A.sort()

len_A = len(A)
ans = 0
for i in range(1, len_A):
    ans += A[len_A - 1 - int(i / 2)]

print(ans)
