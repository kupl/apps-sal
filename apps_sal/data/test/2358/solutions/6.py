S = input()
N = len(S)
L, R = [], []
l, r = 0, N - 1
while r > l:
    while S[l] == ")":
        l += 1
        if l >= N:
            break
    while S[r] == "(":
        r -= 1
        if r < 0:
            break
    if r > l:
        L.append(l + 1)
        R.append(r + 1)
        l += 1
        r -= 1

if len(L) == 0:
    print(0)
else:
    print(1)
    print(len(L) * 2)
    print(*(L + R[::-1]))
