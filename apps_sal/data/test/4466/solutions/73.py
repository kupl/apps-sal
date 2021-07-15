X, Y, Z = list(map(int, input().split()))
ans = 0
for i in range(1, 10 ** 5):
    if X - Y * i - Z * (i + 1) >= 0:
        ans = i
        continue
    else:
        break
print(ans)

