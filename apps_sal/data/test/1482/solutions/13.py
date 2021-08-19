(n, k) = [int(i) for i in input().split()]
data = [int(i) for i in input().split()]
box = [0 for i in range(n * k)]
(a, b) = (0, n * k)
for i in range(k):
    box[data[i] - 1] = 1
    print(data[i], end=' ')
    c = 1
    for j in range(a, b):
        if box[j] == 0 and c < n and (not j + 1 in data):
            print(j + 1, end=' ')
            box[j] = 1
            c += 1
        elif c == n:
            a = j
            break
    print()
