N, K = map(int, input().split())
*X, = map(int, input().split())
A = []
B = []
for x in X:
    if x >= 0:
        A.append(x)
    else:
        B.append(abs(x))
B.sort()
i = min(K, len(A))
j = K - i
ans = []
while i >= 0 and j <= len(B):
    if i == 0:
        ans.append(B[j - 1])
    elif j == 0:
        ans.append(A[i - 1])
    else:
        a, b = A[i - 1], B[j - 1]
        ans.append(a + b + min(a, b))
    i -= 1
    j += 1
print(min(ans))
