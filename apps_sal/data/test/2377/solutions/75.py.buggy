N, H = map(int, input().split())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

max_a = max(A)
B.sort(key=lambda b: -b)  # descending

ans = 0
for b in B:
    if b < max_a:
        break
    H -= b
    ans += 1
    if H <= 0:
        print(ans)
        return
ans += (H - 1) // max_a + 1  # ceil
print(ans)
