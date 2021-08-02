n = int(input())
R = sorted([list(map(int, input().split())) for i in range(n)], key=lambda R: -R[1])
B = sorted([list(map(int, input().split())) for i in range(n)])
ans = 0
for c, d in B:
    for a, b in R:
        if a < c and b < d:
            R.remove([a, b])
            ans += 1
            break
print(ans)
