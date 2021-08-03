n, m = [int(a) for a in input().split()]
x = [int(a) for a in input().split()]
y = [int(a) for a in input().split()]

count = 0
i, j = 0, 0
cand_i, cand_j = x[0], y[0]
while i < n and j < m:
    if cand_i == cand_j:
        count += 1
        i += 1
        j += 1
        if not (i < n and j < m):
            break
        cand_i, cand_j = x[i], y[j]

    elif cand_i > cand_j:
        j += 1
        if not (i < n and j < m):
            break
        cand_j += y[j]
    elif cand_i < cand_j:
        i += 1
        if not (i < n and j < m):
            break
        cand_i += x[i]

print(count)
