(n, m) = map(int, input().split())
votes = [0] * n
for i in range(m):
    row = list(map(int, input().split()))
    rowmax = max(row)
    votes[row.index(rowmax)] += 1
votmax = max(votes)
print(votes.index(votmax) + 1)
