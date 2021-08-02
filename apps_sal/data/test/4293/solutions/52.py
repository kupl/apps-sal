pqr = list(map(int, input().split()))

ans = float("inf")
for i in range(2):
    for j in range(i + 1, 3):
        t = pqr[i] + pqr[j]
        if t < ans: ans = t
print(ans)
