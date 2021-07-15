
N = int(input())
S = input()

ris = [i for i, s in enumerate(S) if s == "R"]
gis = [i for i, s in enumerate(S) if s == "G"]
bis = [i for i, s in enumerate(S) if s == "B"]

all = len(ris) * len(gis) * len(bis)

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        k = 2*j - i
        if 0 <= k < N:
            if S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                cnt += 1

ans = all - cnt


print(ans)

