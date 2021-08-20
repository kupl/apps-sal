(n, x, y) = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
ans = 0
for i in range(n):
    ok = 1
    for j in range(max(0, i - x), min(i + y + 1, n)):
        if j == i:
            continue
        elif A[j] > A[i]:
            continue
        else:
            ok = 0
    if ok:
        ans = i
        break
print(ans + 1)
