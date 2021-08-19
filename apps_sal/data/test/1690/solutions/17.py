input()
S = list(map(int, input().split()))
an = S[-1]
la = S[-1]
for i in range(len(S) - 2, -1, -1):
    ne = max(min(la - 1, S[i]), 0)
    an += ne
    la = ne
print(an)
