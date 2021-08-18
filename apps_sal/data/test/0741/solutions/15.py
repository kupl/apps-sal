n, M = [int(x) for x in input().split()]
arr = [0] + [int(x) for x in input().split()] + [M]
forward, backward = [0], []
[forward.append(forward[i - 1] + arr[i] - arr[i - 1] if i % 2 == 1 else forward[i - 1]) for i in range(1, n + 2)]
mx = forward[-1]
if n % 2 == 0:
    temp = arr[::-1]
    backward = [0]
    [backward.append(backward[i - 1] + temp[i - 1] - temp[i] if i % 2 == 0 else backward[i - 1]) for i in range(1, n + 2)]
else:
    temp = arr[::-1]
    backward = [0]
    [backward.append(backward[i - 1] + temp[i - 1] - temp[i] if i % 2 == 1 else backward[i - 1]) for i in range(1, n + 2)]
backward = backward[::-1]
i = 0
for a, b in zip(arr, arr[1:]):
    res1 = forward[i] + (1 if i % 2 == 0 else b - (a + 1)) + backward[i + 1]
    if a + 1 == b:
        res1 = -1
    res2 = forward[i] + (b - 1 - a if i % 2 == 0 else 1) + backward[i + 1]
    if b - 1 == a:
        res2 = -1
    mx = max(mx, res1, res2)
    i += 1

print(mx)
