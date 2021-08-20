(n, a, b, c) = map(int, input().split())
l = [int(input()) for _ in range(n)]
ans = 100000000000
for i in range(4 ** n):
    A = []
    B = []
    C = []
    D = []
    current = 0
    for j in range(n):
        if i >> 2 * j & 3 == 0:
            A.append(l[j])
        elif i >> 2 * j & 3 == 1:
            B.append(l[j])
        elif i >> 2 * j & 3 == 2:
            C.append(l[j])
        elif i >> 2 * j & 3 == 3:
            D.append(l[j])
    if A and B and C:
        current += (len(A) - 1) * 10 + abs(sum(A) - a)
        current += (len(B) - 1) * 10 + abs(sum(B) - b)
        current += (len(C) - 1) * 10 + abs(sum(C) - c)
        ans = min(ans, current)
print(ans)
