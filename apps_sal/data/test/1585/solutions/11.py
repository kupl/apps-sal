a, b = map(int, input().split())
score = 0
while b >= a:
    a *= 2
    score += 1
print(score)
