n = int(input())
b = [int(i) for i in input().split()]


def binary_search(low, high, search, numbers):
    mid = (low + high) // 2
    if low > high:
        return None
    if numbers[mid] == search:
        return mid
    elif numbers[mid] < search:
        return binary_search(mid + 1, high, search, numbers)
    else:
        return binary_search(low, mid - 1, search, numbers)


d = {}
for i in b:
    if not i in d:
        d[i] = 0
for i in b:
    d[i] += 1
a = []
for i in d:
    a.append(i)
a.sort()
n = len(a)
power = []
wk1 = 1
limit = 2 * max(a) + 1
while wk1 < limit:
    power.append(wk1)
    wk1 *= 2
f = [True] * n
wkl = len(power)
for i in range(n):
    if f[i]:
        wks = len(bin(a[i])) - 3
        for j in range(wks, wkl):
            wk1 = binary_search(0, n - 1, power[j] - a[i], a)
            if wk1 != None:
                if not (wk1 == i and d[a[wk1]] == 1):
                    f[wk1] = False
                    f[i] = False
                    break
ans = 0
for i in range(n):
    if f[i]:
        ans += d[a[i]]
print(ans)
