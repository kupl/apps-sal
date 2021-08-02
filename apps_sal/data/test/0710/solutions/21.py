N = int(input())
S = [ord(c) for c in input()]
TS = [ord(c) for c in 'ACTG']
ans = 1000000000000
for i in range(0, N - 4 + 1):
    ca = 0
    for j in range(4):
        dl = abs(S[i + j] - TS[j])
        ca += min(dl, 26 - dl)
    ans = min(ans, ca)
print(ans)
