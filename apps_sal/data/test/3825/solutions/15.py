n = int(input())
ans = 0
minv = [int(1000000000.0)] * 200000
minv[0] = 0
for i in range(49):
    for j in range(49):
        minv[(4 * i + 9 * j) % 49] = min(minv[(4 * i + 9 * j) % 49], i + j)
for i in range(49):
    if n >= minv[i]:
        ans += n - minv[i] + 1
print(ans)
