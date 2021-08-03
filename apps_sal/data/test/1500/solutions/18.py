n, k = [int(i) for i in input().split()]
R = [int(m) for m in input().split()]
s = 0
point = 0
while point < n - 1:
    possMove = 0
    for i in range(point + 1, n):
        if R[i] - R[point] <= k:
            possMove = i
        else:
            break
    if possMove == 0:
        s = -1
        break
    else:
        s += 1
        point = possMove
print(s)
