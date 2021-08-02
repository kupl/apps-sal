A, B, K = list(map(int, input().split()))
c = 0
S = []
if B - A <= K:
    for i in range(A, B + 1):
        print(i)
    return
for i in range(A, B + 1):
    if c == K:
        break
    print(i)
    S.append(i)
    c += 1
for i in range(B - K + 1, B + 1):
    if i not in S:
        print(i)
