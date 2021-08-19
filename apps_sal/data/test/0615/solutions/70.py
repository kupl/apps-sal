N = int(input())
A = [int(a) for a in input().split()]

S = [0] * N
S[0] = A[0]
for i in range(1, N):
    S[i] = A[i] + S[i - 1]

ans = 2 * 10**14
l = 0
temp = 2 * 10**14
r = 2
# for i in range(2, N):
#    if abs(S[-1]-2*S[i]+S[1]) < temp:
#        temp = abs(S[-1]-2*S[r]+S[1])
#        r = i

for i in range(2, N - 1):
    r = max(r, i)
    while l + 1 < i - 1 and abs(S[i - 1] - 2 * S[l]) > abs(S[i - 1] - 2 * S[l + 1]):
        l += 1
    while r + 1 < N - 1 and abs(S[N - 1] - 2 * S[r] + S[i - 1]) > abs(S[N - 1] - 2 * S[r + 1] + S[i - 1]):
        r += 1
    t = max(S[N - 1] - S[r], S[r] - S[i - 1], S[i - 1] - S[l], S[l]) - min(S[N - 1] - S[r], S[r] - S[i - 1], S[i - 1] - S[l], S[l])
    ans = min(ans, t)

print(ans)
