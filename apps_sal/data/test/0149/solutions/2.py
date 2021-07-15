x, y, l, r = map(int, input().split())
data = []
tx = 1
while (tx < r + 3):
    ty = 1
    while (ty < r + 3):
        data.append(tx + ty)
        ty *= y
    tx *= x
data = sorted(set(data))
data = [elem for elem in data if l <= elem and elem <= r]
data = [l - 1] + data + [r + 1] 
ans = 0
for i in range(1, len(data)):
    ans = max(ans, data[i] - data[i - 1] - 1)
print(ans)
