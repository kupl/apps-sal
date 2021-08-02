S = input()
count = 0


def rec(n):
    if n >= len(S): return 0
    if S[n] == 'A' or S[n] == 'C' or S[n] == 'G' or S[n] == 'T': return rec(n + 1) + 1
    else: return 0


for i in range(len(S)):
    c = rec(i)
    count = max(count, c)
print(count)
