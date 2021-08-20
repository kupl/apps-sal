(n, m, q) = list(map(int, input().split()))


def csum(row):
    return max(list(map(len, ''.join(map(str, row)).split('0'))))


grid = [''.join(input().split()) for i in range(n)]
score = [max(list(map(len, row.split('0')))) for row in grid]
for i in range(q):
    (i, j) = list(map(int, input().split()))
    row = grid[i - 1]
    row = row[:j - 1] + ('1' if row[j - 1] == '0' else '0') + row[j:]
    grid[i - 1] = row
    score[i - 1] = csum(row)
    print(max(score))
