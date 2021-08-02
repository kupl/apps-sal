N, M = map(int, input().split())
H = list(map(int, input().split()))
glaph = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    glaph[A].append(B)
    glaph[B].append(A)

ans = 0
for j in range(N):
    check = True
    for k in glaph[j]:
        if H[j] <= H[k]:
            check = False
            break
    if check:
        ans += 1

print(ans)
