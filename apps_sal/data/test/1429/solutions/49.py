from collections import Counter
N, S = input().split()
N = int(N)
AT, CG = 0, 0
d = Counter()
d[AT, CG] = 1
ans = 0
for i in range(N):
    if S[i] == "A":
        AT += 1
    elif S[i] == "T":
        AT -= 1
    elif S[i] == "C":
        CG += 1
    else:
        CG -= 1
    ans += d[AT, CG]
    d[AT, CG] += 1
print(ans)
