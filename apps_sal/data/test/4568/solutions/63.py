N = int(input())
S = list(input())

res = 0

for i in range(1, N):
    cnt = set(S[0:i]) & set(S[i:N])
    if res < len(cnt):
        res = len(cnt)

print(res)
