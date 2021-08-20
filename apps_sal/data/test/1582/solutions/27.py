from collections import defaultdict
N = int(input())
cnts = defaultdict(int)
for i in range(1, N + 1):
    if i % 10 == 0:
        continue
    digits = []
    while i > 0:
        (i, r) = divmod(i, 10)
        digits.append(r)
    digits = digits[::-1]
    cnts[digits[0], digits[-1]] += 1
ans = 0
for ((head, tail), c1) in list(cnts.items()):
    c2 = cnts.get((tail, head), 0)
    ans += c1 * c2
print(ans)
