(N, H) = list(map(int, input().split()))
B = []
A = 0
for _ in range(N):
    (a, b) = list(map(int, input().split()))
    A = max(A, a)
    B.append(b)
B.sort(reverse=True)
ans = (H - 1) // A + 1
for i in range(N):
    H -= B[i]
    if H <= 0:
        ans = min(ans, i + 1)
        break
    ans = min(ans, (H - 1) // A + 1 + i + 1)
print(ans)
