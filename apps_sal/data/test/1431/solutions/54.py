N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
for i, a in enumerate(A[::-1]):
    n = m = N - i
    s = 0
    while m <= N:
        s += ans[m - 1]
        m += n
    ans[n - 1] = (s % 2) ^ a

ans = [i + 1 for i, a in enumerate(ans) if a]
print(len(ans))
if ans:
    print(*ans, sep='\n')
