(n, k) = list(map(int, input().split()))
row = list(map(int, input().split()))
ranked = list([x[1] for x in sorted([(-x[1], x[0]) for x in enumerate(row)])])
prev = list(range(-1, n - 1))
nxt = list(range(1, n + 1))
teams = [0] * n
current = 1
total = 0
for i in ranked:
    if total > n:
        break
    if not teams[i]:
        teams[i] = current
        took = 1
        count = k
        left = prev[i]
        while count > 0 and left != -1:
            teams[left] = current
            left = prev[left]
            took += 1
            count -= 1
        count = k
        right = nxt[i]
        while count > 0 and right != n:
            teams[right] = current
            right = nxt[right]
            took += 1
            count -= 1
        if left != -1:
            nxt[left] = right
        if right != n:
            prev[right] = left
        total += took
        current = 2 if current == 1 else 1
print(''.join(map(str, teams)))
