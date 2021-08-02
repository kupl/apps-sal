n, m = list(map(int, input().split()))
puzzles = list(map(int, input().split()))

puzzles = sorted(puzzles)
diffs = []
for i in range(len(puzzles) - n + 1):
    diffs.append(puzzles[i + n - 1] - puzzles[i])

print(min(diffs))
