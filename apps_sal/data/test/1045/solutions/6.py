n = int(input())
(H, L) = (0, 1)
while L <= n:
    H += 1
    n -= L
    L += H + 1
print(H)
