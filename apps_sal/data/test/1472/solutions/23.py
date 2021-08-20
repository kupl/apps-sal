(n, x, y) = list(map(int, input().split()))
x -= 1
y -= 1
half = (x + y) // 2
ans = [0] * n
for i in range(n):
    for j in range(i, n):
        if i <= x:
            if j <= half:
                ans[j - i] += 1
            else:
                ans[x - i + 1 + abs(y - j)] += 1
        elif x < i and i <= y:
            ans[min(j - i, i - x + 1 + abs(y - j))] += 1
        else:
            ans[j - i] += 1
for i in range(1, n):
    print(ans[i])
