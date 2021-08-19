(candies, people, m, d) = [int(i) for i in input().split(' ')]
max_score = 0
for t in range(d):
    x = candies // (people * t + 1)
    x = min(x, m)
    score = (t + 1) * x
    if score > max_score:
        max_score = score
print(max_score)
