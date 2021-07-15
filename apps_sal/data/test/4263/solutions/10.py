S=input()
count=0
def rec(n):
    if n >= len(S): return 0
    if S[n] in 'ACGT': return rec(n+1) + 1
    else: return 0
for i in range(len(S)):
    c=rec(i)
    count = max(count, c)
print(count)
