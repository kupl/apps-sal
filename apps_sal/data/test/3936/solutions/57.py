N = int(input())
S = [list(input()) for _ in range(2)]
prev = S[0][0] == S[1][0]
if prev:
    x = 3
    i = 1
else:
    x = 6
    i = 2
while i < N:
    nxt = S[0][i] == S[1][i]
    i += 1 if nxt else 2
    if prev and nxt:
        x *= 2
    elif prev:
        x *= 2
    elif nxt:
        x = x
    else:
        x *= 3
    prev = nxt
print(x % (10**9 + 7))
