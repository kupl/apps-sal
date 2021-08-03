n, a, b, c = list(map(int, input().split()))
L = [int(input()) for _ in range(n)]
ans = 10**9
for x in range(4**n):
    A, B, C = 0, 0, 0
    cost = 0
    for i in range(n):
        r = x % 4
        x //= 4
        if r == 1:
            A += L[i]
        elif r == 2:
            B += L[i]
        elif r == 3:
            C += L[i]
        if r > 0:
            cost += 10
    if A == 0 or B == 0 or C == 0:
        continue
    cost += -30 + abs(A - a) + abs(B - b) + abs(C - c)
    ans = min(ans, cost)
print(ans)
