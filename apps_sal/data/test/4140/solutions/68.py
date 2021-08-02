S = list(input())
f = S[0]
c = 0
for i in range(1, len(S)):
    if i % 2 == 1:
        if f == S[i]:
            c += 1
    else:
        if f != S[i]:
            c += 1
print(c)
