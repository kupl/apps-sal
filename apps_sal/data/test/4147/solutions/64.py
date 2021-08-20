from itertools import product
(n, a, b, c) = map(int, input().split())
l = [int(input()) for i in range(n)]
ans = float('inf')
for choice in product([0, 1, 2, 3], repeat=n):
    items = [0] * 3
    totals = [0] * 3
    temp = 0
    if min([choice.count(i) for i in range(3)]) == 0:
        continue
    for (i, ch) in enumerate(choice):
        if ch == 3:
            continue
        totals[ch] += l[i]
        items[ch] += 1
        if items[ch] > 1:
            temp += 10
    temp += abs(a - totals[0])
    temp += abs(b - totals[1])
    temp += abs(c - totals[2])
    ans = min(ans, temp)
print(ans)
