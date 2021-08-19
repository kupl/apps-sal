(c, d) = list(map(int, input().split()))
(n, m) = list(map(int, input().split()))
k = int(input())
S = 0
if n * m > k:
    nub = n * m - k
    S = 100000000000
    S0 = S
    i = 0
    while S0 <= S and i <= int(nub / n + 2):
        S = S0
        S0 = i * c + d * max(0, nub - n * i)
        i += 1
print(S)
