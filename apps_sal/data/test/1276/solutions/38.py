N = int(input())
S = input()

R = []
G = []
B = []

for i in range(N):
    if S[i] == 'R':
        R.append(i + 1)
    elif S[i] == 'G':
        G.append(i + 1)
    elif S[i] == 'B':
        B.append(i + 1)

lenb = len(B)

cnt = 0
for r in R:
    for g in G:
        up = max(r, g)
        down = min(r, g)
        diff = up - down

        chk = 0
        if up + diff <= N:
            if S[up + diff - 1] == 'B':
                chk += 1
        if down - diff >= 1:
            if S[down - diff - 1] == 'B':
                chk += 1
        if diff % 2 == 0:
            if S[int(up - diff / 2 - 1)] == 'B':
                chk += 1
        cnt += lenb - chk

print(cnt)
