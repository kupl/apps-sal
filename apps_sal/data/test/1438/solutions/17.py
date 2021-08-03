n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

results = [None] * n

for i in range(n):
    div, mod = b[i] // a[i], b[i] % a[i]
    insufficient = a[i] - mod
    results[i] = [div, mod, insufficient, i]


results.sort()

i = 0

while k > 0:
    k -= 1
    index = results[i][3]
    new_insufficient = results[i][2] - 1
    if new_insufficient == 0:
        results[i][0] += 1
        results[i][1] = 0
        results[i][2] = a[index]
    else:
        results[i][1] += 1
        results[i][2] -= 1
    results.sort()

print(results[0][0])
