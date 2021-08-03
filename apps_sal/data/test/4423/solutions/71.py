N = int(input())
R = [input().split() for i in range(N)]

R2 = [{'i': i + 1, 's': R[i][0], 'p':int(R[i][1])} for i in range(N)]

S = []
for r in R:
    if r[0] not in S:
        S.append(r[0])
S.sort()

for s in S:
    rs = [r for r in R2 if r['s'] == s]
    sorted_rs = sorted(rs, key=lambda x: x['p'], reverse=True)
    for r in sorted_rs:
        print(r['i'])
