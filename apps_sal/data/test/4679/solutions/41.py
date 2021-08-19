S = {i: list(input()) for i in 'abc'}
n = 'a'
while S[n]:
    n = S[n].pop(0)
print(n.upper())
