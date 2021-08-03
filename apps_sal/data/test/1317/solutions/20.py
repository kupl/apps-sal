n, m = map(int, input().split())
arr = {}
first = []
times = n // m

for i in range(1, m + 1):
    tmp = i % m
    if tmp != 0:
        tmp *= tmp
        tmp %= m

    tmp2 = arr.get(tmp, 0)
    arr[tmp] = tmp2 + times
    first.append(tmp)

for i in range(n - (times * m)):
    arr[first[i]] += 1

result = 0
for key in arr.keys():
    comp = (m - key) % m
    e1 = arr[key]
    e2 = arr.get(comp, 0)

    if comp != 0 or (m % 2 == 0 and comp != m // 2):
        result += e1 * e2
    else:
        result += (e1 * e1)
print(result)
