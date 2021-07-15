N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
A.sort()
Ans = []
ans = 0
cumA = A[:]
for i in range(N):
    j = i - M
    if j>=0:
        cumA[i] += cumA[j]
for a in cumA:
    ans += a
    Ans.append(ans)
print(" ".join(map(str, Ans)))

