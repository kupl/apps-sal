S = input()
N = len(S)
L = []
temp = S[0]
c = 1
for i in range(1, N - 1):
    if S[i] == temp:
        c += 1
    else:
        L.append(c)
        c = 1
        temp = S[i]
if S[N - 1] == temp:
    c += 1
else:
    L.append(c)
    c = 1
L.append(c)
ans = N
while len(L) >= 3:
    if L[0] > L[-1]:
        ans = min(ans, N - L[-1])
        L[-2] += L[-1]
        L.pop(-1)
    else:
        ans = min(ans, N - L[0])
        L[1] += L[0]
        L.pop(0)
if len(L) == 2:
    ans = min(ans, max(L))
print(ans)
