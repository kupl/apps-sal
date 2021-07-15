N, K = map(int,input().split())
S = input()

#グループの個数
cnt = 1

for i in range(N-1):
    if S[i] != S[i+1]:
        cnt += 1

print(N - max(1, cnt - 2*K))
