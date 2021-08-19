def read_data():
    n = int(input().strip())
    pieces = []
    for j in range(4):
        a = []
        for i in range(n):
            a.append(input().strip())
        if j < 3:
            input().strip()
        pieces.append(a)
    return (n, pieces)


def solve():
    counts = []
    for piece in pieces:
        cur = 0
        sum = 0
        for i in range(n):
            for j in range(n):
                if ord(piece[i][j]) - 48 == cur:
                    sum += 1
                cur += 1
                cur %= 2
        counts.append(sum)
    max = n * n
    counts.sort()
    sum = 0
    for i in range(4):
        if i < 2:
            sum += counts[i]
        else:
            sum += max - counts[i]
    return sum


(n, pieces) = read_data()
print(solve())
