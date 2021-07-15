N, p = list(map(int, input().split()))
A = list(map(int, input().split()))
sa = sum(A)
cursum = 0
ans = 0
for i, a in enumerate(A[:-1]):
    cursum += a
    score = (cursum % p) + ((sa - cursum) % p)
    ans = max(ans, score)

print(ans)

