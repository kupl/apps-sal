n, k1, k2 = map(int, input().split())

A = map(int, input().split())
B = map(int, input().split())

C = [x - y for x, y in zip(B, A)]

k = k1 + k2
for i in range(k):
    if min(C) >= 0:
        C[C.index(max(C))] -= 1
    elif abs(max(C)) <= abs(min(C)):
        C[C.index(min(C))] += 1
    else:
        C[C.index(max(C))] -= 1
ans = 0
for i in C:
    ans += i**2

print(ans)
