(A, B) = list(map(int, input().split()))
ans = 0
for i in range(A, B + 1):
    S = str(i)
    N = len(S)
    if all((S[i] == S[-i - 1] for i in range(N // 2))):
        ans += 1
print(ans)
