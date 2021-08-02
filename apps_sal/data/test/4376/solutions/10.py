n, m = [int(i) for i in input().split()]
rooms = [0] + [int(i) for i in input().split()]
for i in range(2, n + 1):
    rooms[i] += rooms[i - 1]
letters = [int(i) for i in input().split()]
for i in range(m):
    p = 0
    q = n
    while True:
        position = (p + q) // 2
        if rooms[position] < letters[i]:
            p = position
        else:
            q = position
        if q - p <= 1:
            print(q, letters[i] - rooms[p])
            break
