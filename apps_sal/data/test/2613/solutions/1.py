t = int(input())
for _ in range(t):
    (n, k, z) = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    best = -1
    best_pair = -1
    acc = a[0]
    used = 1
    for (prev, cur) in zip(a[:-1], a[1:]):
        used += 1
        if prev + cur > best_pair:
            best_pair = prev + cur
        acc += cur
        if (k - used + 2) // 2 <= z and used <= k + 1:
            score = acc + (k + 1 - used) // 2 * best_pair + (k + 1 - used) % 2 * prev
            if score > best:
                best = score
    print(best)
