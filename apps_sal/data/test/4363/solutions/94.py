(K, S) = map(int, input().split())
ans = 0
x = S // 3 + 1
for i in range(x):
    y = (S - i) // 2 + 1
    for j in range(i, y):
        k = S - i - j
        if k > K:
            continue
        if i == j == k:
            ans += 1
        elif i == j or j == k:
            ans += 3
        else:
            ans += 6
print(ans)
