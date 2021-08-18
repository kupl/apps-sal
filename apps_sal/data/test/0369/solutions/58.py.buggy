N, M = map(int, input().split())
S = list(input())
T = S[::-1]
D = [0] * N
if N <= M:
    print(N)
    return
renzoku, ma = 0, 0
for i in range(1, N + 1):
    if S[i] == '1':
        renzoku += 1
    else:
        ma = max(ma, renzoku)
        renzoku = 0
if ma >= M:
    print(-1)
    return
r = 0
for i in range(1, M + 1):
    if T[i] != '1':
        r = i
ans = [r]

while r + M < N:
    for i in range(M, 0, -1):
        if T[r + i] == '0':
            ans.append(i)
            r += i
            break

ans.append(N - r)
print(*ans[::-1])
