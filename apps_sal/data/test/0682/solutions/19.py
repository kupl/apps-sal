def read():
    return list(map(int, input().split()))


(r1, c1, r2, c2) = read()
L = 1 if r1 == r2 or c1 == c2 else 2
K = max(abs(r1 - r2), abs(c1 - c2))
if abs(r1 - r2) == abs(c1 - c2):
    S = 1
elif (r1 + c1) % 2 == (r2 + c2) % 2:
    S = 2
else:
    S = 0
print(L, S, K)
