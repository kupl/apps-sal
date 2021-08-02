n, m = map(int, input().split())
arr = list(map(int, input().split()))
imos1 = [0] * (m * 2 + 2)
imos2 = [0] * (m * 2 + 2)
imos3 = [0] * (m * 2 + 2)
for i in range(n - 1):
    cost = (m + arr[i + 1] - arr[i]) % m
    if arr[i] < arr[i + 1]:
        imos1[arr[i]] += cost
        imos1[arr[i] + m] -= cost
        imos2[arr[i] + 2] += -1
        imos2[arr[i + 1] + 1] += 1
        imos3[arr[i + 1] + 1] += cost - 1
    else:
        imos1[arr[i]] += cost
        imos1[arr[i] + m] -= cost
        imos2[arr[i] + 2] += -1
        imos2[arr[i + 1] + m + 1] += 1
        imos3[arr[i + 1] + m + 1] += cost - 1
for i in range(1, m * 2 + 2):
    imos2[i] += imos2[i - 1]
for i in range(m * 2 + 2):
    imos1[i] += imos2[i]
    imos1[i] += imos3[i]
for i in range(1, m * 2 + 2):
    imos1[i] += imos1[i - 1]
xs = [0] * (m + 1)
xs[0] = 10**18
for i in range(1, m + 1):
    xs[i] = imos1[i] + imos1[m + i]
print(min(xs))
