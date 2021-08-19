N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = sum(B)
ans = 0
i, j = 0, M - 1
while i < N:
    #print(s, i, j)
    if s <= K:
        ans = max(ans, i + j + 1)
        s += A[i]
        i += 1
    else:
        if j < 0:
            break
        s -= B[j]
        j -= 1
if s <= K:
    ans = max(ans, N + j + 1)
print(ans)
