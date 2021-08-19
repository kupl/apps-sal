(n, m) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Ao = 0
Bo = 0
for a in A:
    if a % 2 == 1:
        Ao += 1
for b in B:
    if b % 2 == 1:
        Bo += 1
Ae = n - Ao
Be = m - Bo
ans = min(Ao, Be) + min(Ae, Bo)
print(ans)
