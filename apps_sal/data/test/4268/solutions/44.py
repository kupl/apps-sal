def dist(ar1, ar2):
    s = 0
    for i in range(len(ar1)):
        s += (ar1[i] - ar2[i]) ** 2
    return (s ** .5).is_integer()


n, d = map(int, input().split())
ans = 0
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if dist(arr[i], arr[j]):
            ans += 1
print(ans)
