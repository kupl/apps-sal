(n, k) = list(map(int, input().split(' ')))
tgt = list(map(int, input().split(' ')))
tgt = sorted(tgt)[::-1]
count = 0
i = 0
cap = k
while i < n:
    ref = tgt[i:i + cap]
    if i + cap >= n:
        count += 2 * max(ref) - 2
        break
    i += cap
    count += 2 * max(ref) - 2
print(count)
