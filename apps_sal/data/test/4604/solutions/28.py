N = int(input())
A = list(map(int, input().split()))

ans = 0
A_test = sorted(list(set(A)))

if N % 2 == 1:
    judge = [i for i in range(0, N, 2)]
    if (A_test == judge) and (A.count(0) == 1):
        ans = 2**(N // 2)
else:
    judge = [i for i in range(1, N, 2)]
    if A_test == judge:
        ans = 2**(N // 2)

ans = ans % (10**9 + 7)
print(ans)
