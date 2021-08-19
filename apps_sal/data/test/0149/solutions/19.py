(x, y, l, r) = list(map(int, input().split()))
A = [l - 1]
for i in range(100):
    if x ** i > r:
        break
    for j in range(100):
        if y ** j > r:
            break
        t = x ** i + y ** j
        if t >= l and t <= r:
            A.append(t)
A.append(r + 1)
A.sort()
ans = 0
for i in range(len(A) - 1):
    ans = max(ans, A[i + 1] - A[i] - 1)
print(ans)
