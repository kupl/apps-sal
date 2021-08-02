n = int(input())
h = [0] + list(map(int, input().split()))
ans, temp = 0, -1
while True:
    for i in range(n + 1):
        if temp == 0 and h[i] != 0:
            ans += 1
        temp = h[i]
        h[i] = max(h[i] - 1, 0)
    if all(v == 0 for v in h):
        break
print(ans)
