N, Z, W = map(int, input().split())
As = list(map(int, input().split()))

max_score = abs(As[-1] - W)
if N >= 2 and max_score < abs(As[-2] - As[-1]):
    max_score = abs(As[-2] - As[-1])

print(max_score)
