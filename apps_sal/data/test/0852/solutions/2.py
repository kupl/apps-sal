t = int(input())
for _ in range(t):
    (n, k, l) = list(map(int, input().split()))
    d = list(map(int, input().split()))
    p = list(range(k)) + list(range(k, 0, -1))
    pos = list(range(2 * k))
    ans = 'Yes'
    for i in range(n):
        new_pos = []
        for t in pos:
            j = 1
            for j in range(1, 2 * k + 1):
                if d[i] + p[(t + j) % (2 * k)] > l:
                    break
                new_pos.append((t + j) % (2 * k))
        pos = list(set(new_pos))
        if len(pos) == 0:
            ans = 'No'
    print(ans)
