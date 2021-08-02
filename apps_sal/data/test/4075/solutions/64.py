N, M = list(map(int, input().split()))
S = [0] * M
answer = 0

for i in range(M):
    S[i] = list(map(int, input().split()))

P = list(map(int, input().split()))

for i in range(2**N):
    mb = '0' + str(N) + 'b'
    bi = format(i, mb)
    count = 0
    for j in range(M):
        on = 0
        for k in range(S[j][0]):
            on += int(bi[-S[j][k + 1]])
        if on % 2 == P[j]:
            count += 1
    if count == M:
        answer += 1

print(answer)
