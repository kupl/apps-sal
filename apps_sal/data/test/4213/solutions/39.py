import itertools
N = int(input())
A = map(int, input().split())
score = 0
for i, j in list(itertools.combinations(A, 2)):
    if score < abs(i - j): score = abs(i - j)
print(score)
