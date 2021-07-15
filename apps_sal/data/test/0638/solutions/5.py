n,m = list(map(int,input().split()))
A = [int(x) for x in input().split()]

R = []
S = []
for a in A:
    s = sum(S)
    i = len(S)
    while s + a > m:
        i -= 1
        s -= S[i]
    R.append(len(S) - i)
    S.append(a)
    S.sort()

print(*R)

