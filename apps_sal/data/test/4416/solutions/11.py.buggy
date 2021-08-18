n, k = map(int, input().split())
A, B, both = [0], [0], [0]
for i in range(n):
    t, a, b = map(int, input().split())
    if a == 1 and b == 1:
        both.append(t)
    if a == 1 and b == 0:
        A.append(t)
    if a == 0 and b == 1:
        B.append(t)
A.sort()
B.sort()
both.sort()
if len(A) - 1 + len(both) - 1 < k or len(B) - 1 + len(both) - 1 < k:
    print(-1)
    return

for i in range(1, len(A)):
    A[i] += A[i - 1]
for i in range(1, len(B)):
    B[i] += B[i - 1]
cur = 0
ans = 10**12 + 10
for ch in range(len(both)):
    cur += both[ch]
    if ch > k:
        break
    # Need k - ch each from A and B
    if k - ch < len(A) and k - ch < len(B):
        ans = min(ans, A[k - ch] + B[k - ch] + cur)
print(ans)
