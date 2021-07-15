def janken(sa,sb):
    if (sa=="R" and sb=="S") or (sa=="S" and sb=="R"):return "R"
    if (sa=="P" and sb=="R") or (sa=="R" and sb=="P"):return "P"
    if (sa=="S" and sb=="P") or (sa=="P" and sb=="S"):return "S"
    if sa==sb:return sa

n,k = list(map(int,input().split()))
s = input()

memo = [list(s)] + [[None]*n for _ in range(k)]

for i in range(1,k+1):
    for j in range(n):
        sa = memo[i-1][j]
        sb = memo[i-1][(j+2**(i-1))%n]
        memo[i][j] = janken(sa,sb)
print((memo[k][0]))

