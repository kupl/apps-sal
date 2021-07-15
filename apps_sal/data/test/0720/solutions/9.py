import sys
N = int(input())
count = 1
score_a, score_b = 0, 0

for a, b in (map(int, l.split()) for l in sys.stdin):
    if score_a > score_b:
        score_b = min(score_a, b)
        if score_a == score_b:
            count += 1
    elif score_a < score_b:
        score_a = min(score_b, a)
        if score_a == score_b:
            count += 1

    if score_a < min(a, b):
        count += min(a, b) - score_a

    score_a, score_b = a, b

print(count)
