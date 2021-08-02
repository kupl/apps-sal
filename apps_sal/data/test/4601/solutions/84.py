N, K = list(map(int, input().split(" ")))
H = sorted(list(map(int, input().split(" "))), reverse=True)
Z = 0
R = 0
for n, e in enumerate(H):
    if (n == K):
        Z = n
        break
    elif (K >= len(H)):
        Z = len(H)
        break
for i in H[Z:]:
    R += i
print(R)
