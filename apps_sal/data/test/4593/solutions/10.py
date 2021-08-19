X = int(input())
ans = 0
for i in range(1, int(X ** 0.5) + 1):
    for j in range(2, 1000):
        tmp = pow(i, j)
        if tmp > X:
            break
        ans = max(ans, tmp)
print(ans)
