(n, k) = list(map(int, input().split()))
a = list(map(int, input().split()))
divs = {}
handled = [False] * k
for x in a:
    divs[x % k] = divs.get(x % k, 0) + 1
result = divs.get(0, 0) - divs.get(0, 0) % 2
for i in range(1, k):
    if not handled[i] and (not handled[k - i]):
        if i != k - i:
            result += 2 * min(divs.get(i, 0), divs.get(k - i, 0))
        else:
            result += divs.get(i, 0) - divs.get(i, 0) % 2
        handled[i] = handled[k - i] = True
print(result)
