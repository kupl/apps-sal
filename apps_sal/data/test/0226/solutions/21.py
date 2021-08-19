n = int(input())
a = [int(i) for i in input().split()]
score = a[n - 1]
total = a[n - 1]
for i in range(n - 2, -1, -1):
    new_score = a[i] + total - score
    if new_score > score:
        score = new_score
    total += a[i]
print(total - score, score)
