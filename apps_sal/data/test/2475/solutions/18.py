n = int(input())
a = [int(item) for item in input().split()]

ans = 0
for c in range(1, n):
    visited = set([0, n - 1])
    total = 0
    for k in range(1, n):
        odd = n - 1 - k * c
        even = k * c
        if even >= n - 1:
            break
        if odd < c:
            break
        if even in visited:
            break
        visited.add(even)
        if odd in visited:
            break
        visited.add(odd)
        total += a[odd] + a[even]
        ans = max(ans, total)
        # print(c, k, total)
        # print(visited)
print(ans)
