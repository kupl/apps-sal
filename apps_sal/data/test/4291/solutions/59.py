N, Q = list(map(int, input().split()))
S = input()

cs = [0] * N
cnt = 0
for i in range(1, N):
    if S[i - 1:i + 1] == "AC":
        cnt += 1
    cs[i] = cnt

for i in range(Q):
    l, r = list(map(int, input().split()))
    print((cs[r - 1] - cs[l - 1]))
