N = int(input())
S = input()
numE = [0] * N
numW = [0] * N
for i in range(N):
    if S[i] == 'E':
        numE[i] += 1
    else:
        numW[i] += 1
    if 0 < i:
        numE[i] += numE[i - 1]
        numW[i] += numW[i - 1]
ans = N
for i in range(N):
    if i == 0:
        val = numE[-1] - numE[i]
    elif i == N - 1:
        val = numW[i - 1]
    else:
        val = numE[-1] - numE[i] + numW[i - 1]
    ans = min(ans, val)
print(ans)
