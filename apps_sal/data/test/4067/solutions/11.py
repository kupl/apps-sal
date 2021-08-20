from collections import Counter
N = int(input())
balanced = N // 3
s = list(map(int, list(input())))
counter = Counter(s)
if counter[0] < balanced:
    for (i, n) in enumerate(s):
        if n > 0 and counter[n] > balanced:
            s[i] = 0
            counter[n] -= 1
            counter[0] += 1
        if counter[0] == balanced:
            break
if counter[2] < balanced:
    for (i, n) in zip(range(N - 1, -1, -1), s[::-1]):
        if n != 2 and counter[n] > balanced:
            s[i] = 2
            counter[n] -= 1
            counter[2] += 1
        if counter[2] == balanced:
            break
if counter[1] < balanced:
    for (i, n) in enumerate(s):
        if n == 2 and counter[2] > balanced:
            s[i] = 1
            counter[2] -= 1
            counter[1] += 1
        if counter[1] == balanced:
            break
if counter[1] < balanced:
    for (i, n) in zip(range(N - 1, -1, -1), s[::-1]):
        if n == 0:
            s[i] = 1
            counter[1] += 1
        if counter[1] == balanced:
            break
print(*s, sep='')
