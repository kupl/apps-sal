N, S = input().split()
N, a = int(N), 0

for i in range(N):
    c1, c2 = 0, 0
    for s in S[i:]:
        if s == 'A':
            c1 += 1
        if s == 'T':
            c1 -= 1
        if s == 'C':
            c2 += 1
        if s == 'G':
            c2 -= 1
        if c1 == 0 and c2 == 0:
            a += 1
print(a)
