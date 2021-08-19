(N, Z, W) = map(int, input().split())
a_ls = list(map(int, input().split()))
iA = [0] * N
iB = [0] * N
iA[N - 1] = abs(a_ls[N - 2] - a_ls[N - 1])
iB[N - 1] = abs(a_ls[N - 2] - a_ls[N - 1])
for i in range(N - 2, -1, -1):
    if i != 0:
        prev = a_ls[i - 1]
    else:
        prev = W
    ans = -float('inf')
    for j in range(i + 1, N):
        ans = max(ans, iB[j])
    ans = max(ans, abs(prev - a_ls[-1]))
    iA[i] = ans
    if i != 0:
        prev = a_ls[i - 1]
    else:
        prev = Z
    ans = float('inf')
    for j in range(i + 1, N):
        ans = min(ans, iA[j])
    ans = min(ans, abs(prev - a_ls[-1]))
    iB[i] = ans
if N != 1:
    print(iA[0])
else:
    print(abs(W - a_ls[0]))
