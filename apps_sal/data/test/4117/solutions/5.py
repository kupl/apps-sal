N = int(input())
L = sorted(list(map(int, input().split())))
ans = 0
for i in range(N - 2):
    side1 = L[i]
    for j in range(i + 1, N - 1):
        side2 = L[j]
        if side1 == side2:
            continue
        lim = side1 + side2
        for k in range(j + 1, N):
            side3 = L[k]
            if side3 >= lim:
                break
            if side3 != side2:
                ans += 1

print(ans)
