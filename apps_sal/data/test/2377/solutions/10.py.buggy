N, H = list(map(int, input().split()))
B = []
A = 0
for _ in range(N):
    a, b = list(map(int, input().split()))
    A = max(A, a)
    B.append(b)
B = sorted(B, reverse=True) + [0]

i = 0
while B[i] >= A:
    i += 1
B = B[:i]

ans = 0
for i in range(len(B)):
    H -= B[i]
    ans += 1
    if H <= 0:
        print(ans)
        return
print((ans + (H - 1) // A + 1))
