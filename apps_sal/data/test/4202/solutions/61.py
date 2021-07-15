L, R = list(map(int, input().split()))
ans = 2018
for i in range(L, R):
    for j in range(i + 1, R + 1):
        a = (i * j) % 2019
        if a < ans:
            ans = a
        if ans == 0:
            break
    else:
        continue
    break
print(ans)

