n, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
data = data[::-1]
ans = 1

prev = data[0]

for i in range(1, n):
    if not (data[i] != prev and data[i] + k >= prev):
        ans += 1

    if i < n - 1 and data[i] == data[i + 1]:
        prev = prev
    else:
        prev = data[i]

print(ans)
