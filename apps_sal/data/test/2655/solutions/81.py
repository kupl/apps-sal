n = int(input())
A = list(map(int, input().split()))
if n == 2:
    print(max(A))
else:
    A.sort(reverse=True)
    ans = A[0]
    for a in A[1:n // 2]:
        ans += 2 * a
    if n % 2 == 1:
        ans += A[n // 2]
    print(ans)
