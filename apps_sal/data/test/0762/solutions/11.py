(n, b) = map(int, input().split())
arr = list(map(int, input().split()))
ne = 0
ch = 0
mass = []
for i in range(n - 1):
    if arr[i] % 2 == 0:
        ch += 1
    else:
        ne += 1
    if ch == ne:
        mass.append(abs(arr[i] - arr[i + 1]))
ans = 0
mass.sort()
for i in mass:
    if i <= b:
        b -= i
        ans += 1
print(ans)
