def grimper(M):
    k = 1
    while M[k] < M[k - 1]:
        (M[k], M[k - 1]) = (M[k - 1], M[k])
        k += 1
    k = n - 1
    while M[k] < M[k - 1]:
        (M[k], M[k - 1]) = (M[k - 1], M[k])
        k -= 1
    return M


n = int(input())
M = list(map(int, input().split()))
s = sum(M)
m = s // n
if s % n:
    c = 1
else:
    c = 0
r1 = 0
r2 = 0
for k in range(n):
    if M[k] < m:
        r1 += m - M[k]
    if M[k] > m + c:
        r2 += M[k] - (m + c)
print(max([r1, r2]))
